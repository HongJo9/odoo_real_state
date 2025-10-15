from odoo import models, fields, api

class EstatePropertyInherit(models.Model):
    _inherit = "estate.property" #usaremos ese modulo para agregar un nuevo campo
    
    reserved = fields.Boolean(string="Reservado", default=False)
    
    
    # Este método se ejecuta cada vez que se crea un nuevo registro de propiedad.
    @api.model
    def create(self, vals):
        record = super().create(vals)
        if record.state == 'new':
            record.message_post(body="Nueva propiedad registrada")
        return record
    
    ###########################################################################s
    
    