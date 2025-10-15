from odoo import models, fields

class estate_property_tag(models.Model):
    _name = "estate.property.tag"
    _description = "Etiqueta de la Propiedad Inmobiliaria"
    _order = "name"

    name = fields.Char(string="Nombre", required=True)
    property_ids = fields.Many2many("estate.property", string="Propiedades")
    color = fields.Integer(string="Color") 
    
    _sql_constraints = [
        ('unique_tag_name',
         'UNIQUE(name)',
         'El nombre de la etiqueta debe ser único.')
    ]