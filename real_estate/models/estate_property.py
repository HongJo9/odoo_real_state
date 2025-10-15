from odoo import fields, models, api
# from datetime import timedelta # trabajar dias, horas, minutos, segundos
from dateutil.relativedelta import relativedelta #  years, months, days, leapdays, weeks, hours, minutes, seconds, microseconds,
from odoo.exceptions import UserError, ValidationError
from odoo.tools.float_utils import float_compare, float_is_zero

class EstateProperty(models.Model):
    _name = "estate.property"
    _description = "Propiedad Inmobiliaria"
    _order = "id desc"
    _inherit = ['mail.thread', 'mail.activity.mixin'] 

    # Campos básicos
    name = fields.Char(default="Casita" , required=True)
    last_seen = fields.Datetime("Last Seen", default=fields.Datetime.now)
    description = fields.Text(string="Descripción")
    postcode = fields.Char(string="Código Postal")
    date_availability = fields.Date(string="Fecha de Disponibilidad", copy=False, default=fields.Date.today() + relativedelta(months=3))
    expected_price = fields.Float(string="Precio Esperado", copy=False)
    selling_price = fields.Float(string="Precio de Venta", readonly=True, copy=False)
    active = fields.Boolean(string="Active", default=True)
    bedrooms = fields.Integer(string="Dormitorios", default=2)
    living_area = fields.Integer(string="Área de Estar (m²)")
    facades = fields.Integer(string="Fachadas")
    garage = fields.Boolean(string="¿Tiene Cochera?")
    garden = fields.Boolean(string="¿Tiene Jardín?")
    living_area = fields.Float(string="Living Area")
    garden_area = fields.Float(string="Garden Area")
    total_area = fields.Float(string="Total Area", compute="_compute_total_area", store=True)
    
    garden_orientation = fields.Selection(
        string="Orientación del Jardín",
        selection=[
            ('north', 'Norte'),
            ('south', 'Sur'),
            ('east', 'Este'),
            ('west', 'Oeste'),
        ],
        help="Selecciona hacia dónde está orientado el jardín"
    )
    state = fields.Selection(
        string= "Estado",
        selection=[
            ("new", "Nuevo"),
            ("offer_received", "Oferta Recibida "),
            ("offer_accepted", "Oferta Aceptada"),
            ("sold", "Vendida"),
            ("canceled", "Cancelada"),
        ],
        default='new',
        copy= False,
        required=True,
        readonly=True,
    )
    # CAMPOS CON RELACIONES
    property_type_id = fields.Many2one(comodel_name="estate.property.type", string="Tipo de Propiedad")
    # vendedor
    seller_id = fields.Many2one(comodel_name="res.users", string="Vendedor", default=lambda self: self.env.user, readonly=True)
    # comprador
    buyer_id = fields.Many2one(comodel_name="res.partner", string="Comprador", readonly=True)
    #etiquetas
    tag_ids = fields.Many2many("estate.property.tag", string="Etiquetas")
    #datos del modelo ofertas que usare aqui
    offer_ids = fields.One2many(comodel_name="estate.property.offer", inverse_name="property_id", string="Offers")
    
    _sql_constraints = [
        ('expected_price_positive','CHECK (expected_price > 0)','El precio esperado debe ser mayor que cero.'),
        ('selling_price_positive','CHECK (selling_price >= 0)','El precio de venta no puede ser negativo.'),
    ]
    
    @api.ondelete(at_uninstall=False)
    def check_state_before_delete(self):
        # self puede contener varios registros
        for prop in self:
            if prop.state not in ('new', 'canceled'):
                raise ValueError(   
                    f"No se puede eliminar la propiedad '{prop.name}' porque su estado es '{prop.state}'"
                )
    
    @api.depends('living_area', 'garden_area')
    def _compute_total_area(self):
        for record in self:
            record.total_area = (record.living_area or 0.0) + (record.garden_area or 0.0)


    best_price = fields.Float(string="Best Offers", compute="_compute_best_price", store=True)

    @api.depends('offer_ids.price')
    def _compute_best_price(self):
        for record in self:
            offer_prices = record.offer_ids.mapped('price')
            record.best_price = max(offer_prices) if offer_prices else 0.0

    garden = fields.Boolean(string="Garden")
    garden_area = fields.Integer(string="Garden Area")
    garden_orientation = fields.Selection(
        [
            ('north', 'North'),
            ('south', 'South'),
            ('east', 'East'),
            ('west', 'West')
        ],
        string="Orientation"
    )

    @api.onchange('garden')
    def _onchange_garden(self):
        if self.garden:
            # Si se activa el jardín
            self.garden_area = 10
            self.garden_orientation = 'north'
        else:
            # Si se desactiva, se limpian los valores
            self.garden_area = 0
            self.garden_orientation = False

    def action_cancel(self):
        for record in self:
            if record.state == 'sold':
                raise UserError("No puedes cancelar una propiedad vendida")
            record.state='canceled'

    def action_sold(self):
        for record in self:
            if record.state == 'canceled':
                raise UserError("Una propiedad vendida no se puede cancelar")
            record.state='sold'
            
    @api.constrains('expected_price', 'selling_price')
    def _check_selling_price(self):
        for record in self:
            # Si el precio de venta es cero (propiedad aún no vendida), no validar
            if float_is_zero(record.selling_price, precision_digits=2):
                continue

            # Si el precio esperado es 0, no tiene sentido comparar
            if float_is_zero(record.expected_price, precision_digits=2):
                continue

            # Comparar: selling_price < 90% del expected_price
            if float_compare(record.selling_price, record.expected_price * 0.9, precision_digits=2) < 0:
                raise ValidationError(
                    "El precio de venta no puede ser inferior al 90% del precio esperado."
                )