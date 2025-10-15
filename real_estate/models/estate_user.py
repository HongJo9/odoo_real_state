from odoo import models, fields

class ResUsers(models.Model):
    _inherit = 'res.users' # ✅ extendemos el modelo existente, Le dice a Odoo: “Voy a agregar cosas nuevas al modelo de usuarios.”
    
    
    #Aqui estoy declarando un nuevo campo para el modelo users, y a la vez estoy amarrando con el de propiedades
    property_ids = fields.One2many('estate.property', 'seller_id', string='Propiedades', domain="[('state','=','available')]")