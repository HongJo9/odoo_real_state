from odoo import models, fields, api

class ShopProduct(models.Model):
    _name = "shop.product" # nombre tecnico del modelo (unico en odoo)
    _description = "Producto de la tienda"
    
    #Campos del modelo
    name = fields.Char(string="Nombre del producto", required="True", help="Nombre comercial del producto")
    price = fields.Float(string="Precio", required="True", help="Precio unitario del producto")
    available = fields.Boolean(string="Disponible", compute="_compute_available", store=True, readonly=True, help="Indica si el producto está disponible (según su stock)")
    description = fields.Text(string="Descripcion", help="Descripcion del producto (Opcional)")
    stock = fields.Integer(string="Stock disponible", default=0, help="Cantidad de unidades disponibles en el inventario")
    
    #Campo calculado(Precio con IGV)
    price_with_tax = fields.Float(string="Precion con IGV", compute="_compute_price_with_tax", store=True, readonly="1")
    
    # Calcula el precio con IGV (18%)
    @api.depends("price")
    def _compute_price_with_tax(self):
        for product in self:
            product.price_with_tax = product.price * 1.18
            
    @api.depends("stock")
    def _compute_available(self):
        for product in self:
            product.available = product.stock > 0