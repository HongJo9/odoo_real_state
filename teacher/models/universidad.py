from odoo import models, fields

class Universidad(models.Model):
    _name = 'universidad'
    _description = 'Universidad'

    name = fields.Char(string='Nombre', required=True)
    direccion = fields.Char(string='Dirección')
    telefono = fields.Char(string='Teléfono')
    email = fields.Char(string='Email')
    website = fields.Char(string='Sitio Web')
    # teacher_ids = fields.One2many(comodel_name='teacher', inverse_name='universidad_id', string='Profesores')