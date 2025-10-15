from odoo import models

class EstateProperty(models.Model):
    _inherit = 'estate.property' #Hredamos el modelo original
    
    def action_sold(self):
        #Punto de prueba para ver que se ejecuta el override
        print("Override de action_sold: se ha llamado")
        #breakpoint() #tambien puedes usar un depurador si quieres
        result = super().action_sold() #llamamos al metodo original
    
        invoice_vals = {
            'move_type' : 'out_invoice', # tipo factura cliente
            'partner_id' : self.buyer_id.id, # a quién va dirigida la factura.
            'invoice_line_ids': [                   # Aquí se agregan las líneas de factura
                (0, 0, {                           # Primera línea: comisión 6%
                    'name': 'Comisión 6% del precio de venta',
                    'quantity': 1,
                    'price_unit': self.selling_price * 0.06,
                }),
                (0, 0, {                           # Segunda línea: tarifa administrativa
                    'name': 'Tarifa administrativa',
                    'quantity': 1,
                    'price_unit': 100.00,
                }),
            ],
        }
        
        invoice = self.env['account.move'].create(invoice_vals)
        
        print(f"Factura creada con ID: {invoice.id} para el cliente {self.buyer_id.name}")
        
        return result