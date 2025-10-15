{
    'name': "Teacher",
    'version': '1.0',
    'depends': ['base'],
    'author': "Luis",
    'category': 'Category',
    'description': """,
    Modulo de profesores para saber quien es el profesor de cada asignatura
    """,
    # data files always loaded at installation
    'data': [
        # 'views/mymodule_view.xml',
        'security/ir.model.access.csv',
        'views/teacher_views.xml',
        'views/nivel_academico.xml',
        'views/lugar_de_trabajo.xml',
        'views/universidad.xml',
    ],
    'installable': True,
    "application": True,
        
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
}