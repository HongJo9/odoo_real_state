from odoo import models, fields, api

class ResUser(models.Model):
    _inherit = 'res.users'
    
    peso = fields.Float(string="Peso de usuario")
    
    estado_peso  = fields.Selection(string="Estado de salud (PESO)", selection=[
        ('desnutrido', 'Desnutrido'),
        ('normal', 'Peso Normal'),
        ('sobrepeso', 'Sobrepeso'),
    ], compute="_compute_estado", store=False, )
    
    
# ...
    @api.depends('peso')
    def _compute_estado(self):
        for record in self:
            if record.peso < 60:
                record.estado_peso = 'desnutrido'
            # Si no es desnutrido (es decir, peso >= 60)
            elif record.peso >= 60 and record.peso < 80: # Asumimos normal hasta 80
                record.estado_peso = 'normal'
            # Si no es desnutrido ni normal (es decir, peso >= 80)
            else:
                record.estado_peso = 'sobrepeso'