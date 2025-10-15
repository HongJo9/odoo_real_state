from odoo import fields, models, api

class EstatePropertyType(models.Model):
    _name = "estate.property.type"
    _description = "Tipo de Propiedad Inmobiliaria"
    _order = "sequence, name"

    name = fields.Char(string="Nombre", default="House", required=True)
    sequence = fields.Integer(string="Secuencia", default=1)
    property_ids = fields.One2many("estate.property", "property_type_id", string="Propiedades" )
    offer_ids = fields.One2many("estate.property.offer", "property_type_id", string="Ofertas")
    offer_count = fields.Integer(string="Numero de Ofertas Contadas", compute="_compute_offer_count")
    
    @api.depends("offer_ids")
    def _compute_offer_count(self):
        for record in self:
            if record.offer_ids:
                record.offer_count = len(record.offer_ids)
            else:
                record.offer_count = 0
        
    _sql_constraints = [
        ('unique_type_name',
         'UNIQUE(name)',
         'El nombre del tipo de propiedad debe ser único.')
    ]