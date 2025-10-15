{
    'name' : 'User Peso',
    'version' : '1.0',
    'summary' : 'Integracion entre Usuario, propiedad y factura',
    'description' : 'Modulo para agregar nuevo campo peso y sea dinamico',
    'category' : 'peso',
    'depends' : ['real_estate', 'base'],
    'data' : [
        'views/estate_user_view_inherit.xml',
    ],
    'installable' : True,
    'application' : False,
}