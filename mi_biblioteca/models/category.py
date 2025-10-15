from odoo import models, fields

class category(models.Model):
    _name = "mi_biblioteca.category"
    _description = "Categoría de Libro"

    name = fields.Char("Nombre", required=True)          # etiqueta "Nombre", obligatorio
    description = fields.Text("Descripción")             # texto libre
    libro_ids = fields.Many2many("mi_biblioteca.libro", string="Libros")  # relación muchos a muchos con libros

