from odoo import models, fields, api
from datetime import timedelta
from odoo.exceptions import UserError

class estate_property_offer(models.Model):
    _name = "estate.property.offer"
    _description = "Oferta de la Propiedad Inmobiliaria"
    _order = "price desc" #de mayor a menor

    price = fields.Float(string="Precio")
    status = fields.Selection([
        ('pending', 'Pendiente'),
        ('accepted', 'Aceptado'),
        ('refused', 'Rechazado'),
    ], string="Estado", default="pending", copy="False")
    partner_id = fields.Many2one(comodel_name="res.partner", string="Comprador", required=True)
    property_id = fields.Many2one(comodel_name="estate.property", string="Propiedad", required=True, ondelete='cascade')

    validity = fields.Integer(string="Validity (days)", default=7)
    date_deadline = fields.Date(string="Fecha Limite", compute="_compute_date_deadline", inverse="_inverse_date_deadline", store=True)
    
    property_type_id = fields.Many2one("estate.property.type", related = "property_id.property_type_id", store=True)

    # metodo compute
    @api.depends('validity', 'create_date')
    def _compute_date_deadline(self):
        for record in self:
            create_date = record.create_date or fields.Datetime.now()
            record.date_deadline = create_date.date() + timedelta(days=record.validity)
    
    # metodo inverse
    def _inverse_date_deadline(self):
        for record in self:
            if record.create_date and record.date_deadline:
                delta = record.date_deadline - record.create_date.date()
                record.validity = delta.days
            else:
                record.validity = 7

    def action_accept(self):
        for offer in self:
            property = offer.property_id  
            if property.buyer_id:
                raise UserError("Esta propiedad ya tiene un comprador")    
            if offer.status == 'refused':
                raise UserError("No se puede aceptar un oferta rechazada")
            self.status = 'accepted'
            property.buyer_id = offer.partner_id
            property.selling_price = offer.price
            property.state = 'offer_accepted'

    def action_refuse(self):
        for offer in self:
            if offer.status == 'accepted':
                raise UserError("No se puede rechazar una oferta aceptada")
            self.status = 'refused'
    
    @api.model
    def create(self, vals):
        # Compatibilidad: si Odoo pasa una lista, toma el primer elemento
        if isinstance(vals, list):
            vals = vals[0]

        property = self.env['estate.property'].browse(vals['property_id'])
        max_price = max(property.offer_ids.mapped('price'), default=0)

        if vals['price'] <= max_price:
            raise UserError(f"No puedes hacer una oferta menor o igual a la existente ({max_price})")

        property.state = 'offer_received'

        return super().create(vals)
    
    
    _sql_constraints = [
        ('check_offer_price_positive',
         'CHECK(price > 0)',
         'El precio de la oferta debe ser estrictamente positivo.'),
    ]