{
    'name': 'OWL PORTAL',
    'version': '1.0',
    'summary': 'Ejemplo de owl portal',
    'category': 'category',
    'author': 'HongJo',
    'depends': ['base'],
    'data': [
        # Aquí van tus vistas XML si las tienes
        # 'views/standalone_app.xml',
    ],
    'assets': {
        'my_owl_new.assets_standalone_app': [
            ('include', 'web._assets_helpers'),
            'web/static/src/scss/pre_variables.scss',
            'web/static/lib/bootstrap/scss/_variables.scss',
            ('include', 'web._assets_bootstrap'),
            ('include', 'web._assets_core'),
            'my_owl_new/static/src/standalone_app/**/*',
        ],
    },
    'installable': True,
    'auto_install': False,
}
