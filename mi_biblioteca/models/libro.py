from odoo import models, fields

class Libro(models.Model):
    _name = "mi_biblioteca.libro"       # identificador técnico del modelo
    _description = "Libro"              # descripción legible

    name = fields.Char("Título", required=True)          # etiqueta "Título", obligatorio


    fecha_publicacion = fields.Date("Fecha de publicación")  # fecha
    paginas = fields.Integer("Número de páginas")       # entero
    disponible = fields.Boolean("Disponible", default=True)  # booleano con valor por defecto

    author_id = fields.Many2one("mi_biblioteca.author", string="Autor", readonly=True)  # relación muchos a uno con autor
    category_ids = fields.Many2many("mi_biblioteca.category", string="Categorías")  # relación muchos a muchos con categorías