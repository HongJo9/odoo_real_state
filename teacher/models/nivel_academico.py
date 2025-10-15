from odoo import models, fields

class NivelAcademico(models.Model):
    _name = 'nivel.academico'
    _description = 'Nivel Académico'


    name = fields.Char(string='Nivel Académico', required=True)
    # name = fields.Selection([
    #     ('titulado', 'Titulado'),
    #     ('maestria', 'Maestría'),
    #     ('doctorado', 'Doctorado'),
    # ], string='Nivel Académico', required=True)