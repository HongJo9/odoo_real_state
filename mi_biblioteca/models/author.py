from odoo import models, fields

class author(models.Model):
    _name = "mi_biblioteca.author"
    _description = "Autor de Libro"

    name = fields.Char("Nombre", required=True)
    libros_ids = fields.One2many("mi_biblioteca.libro", "author_id", string="Libros")  # relación uno a muchos con libros

