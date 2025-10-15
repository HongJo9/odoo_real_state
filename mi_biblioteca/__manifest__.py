{
    'name': 'Mi Biblioteca',                     # Nombre del módulo que se muestra en la interfaz de Odoo.
    'version': '1.0',                            # Versión del módulo; útil para gestión de actualizaciones.
    'author': 'Luis',                            # Autor o mantenedor del módulo.
    'category': 'Library',                       # Categoría bajo la que aparece en la lista de aplicaciones.
    'summary': 'Gestión sencilla de libros',     # Resumen corto que describe la funcionalidad del módulo.
    'depends': ['base'],                         # Lista de módulos de los que depende (se cargan antes).
    'data': [                                    # Lista de archivos de datos que Odoo cargará al instalar.
        'security/ir.model.access.csv',          # Archivo CSV con reglas de acceso (permisos) para modelos.
        'views/libro_views.xml',
        'views/author_views.xml',
        'views/category_views.xml',                # Vistas (formulario, lista, etc.) definidas en XML.
    ],
    'installable': True,                         # Permite que el módulo sea instalable en la instancia.
    'application': True,                         # Marca el módulo como "aplicación" (aparece en el tablero de apps).
}
