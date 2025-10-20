{
    'name': 'OWL Portal',
    'version': '1.0',
    'summary': 'Ejemplo de OWL en el portal',
    'category': 'Website',
    'author': 'HongJo',
    'depends': ['base', 'portal', 'web'],  # necesario aunque no lo mencione
    'data': [
        'views/portal_my_home.xml',
    ],
    'assets': {
        'web.assets_frontend': [
            'owl_portal/static/src/portal_component/**/*',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
}
