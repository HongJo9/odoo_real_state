from odoo import models, fields

class LugarDeTrabajo(models.Model):
    _name = 'lugar.de.trabajo'
    _description = 'Lugar de Trabajo'

    name = fields.Char(string='Lugar de Trabajo', required=True)