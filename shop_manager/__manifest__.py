{
    "name": "Shop Manager",
    "version": "1.0.0",
    "summary": "Módulo de práctica para gestionar productos y pedidos",
    "description": """
        Módulo para manejar productos, clientes y pedidos como ejemplo de aprendizaje.
    """,
    "category": "Sales",
    "author": "Hong Jo",
    "depends": [
        "base",       # módulo base de Odoo
    ],
    "data": [
        # archivos XML que cargaremos inicialmente (vistas, seguridad, data)
        "security/ir.model.access.csv",
        "views/shop_product_views.xml",
        "views/menus.xml",
        # después agregaremos otras vistas
    ],
    "demo": [
        "data/demo_products.xml",
    ],
    "installable": True,
    "application": True,
    "auto_install": False,
}
