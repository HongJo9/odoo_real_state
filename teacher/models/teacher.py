from odoo import models, fields

class Teacher(models.Model):
    _name = 'teacher'
    _description = 'Teacher'

    name = fields.Char(string='Nombre', required=True)
    edad = fields.Integer(string='Edad')
    asignatura = fields.Char(string='Asignatura', required=True)
    email = fields.Char(string='Email')
    nivel_academico_id = fields.Many2one(comodel_name='nivel.academico', string='Nivel Académico')
    lugar_de_trabajo_id = fields.Many2one(comodel_name='lugar.de.trabajo', string='Lugar de Trabajo')
    universidad_id = fields.Many2one(comodel_name='universidad', string='Universidad')

