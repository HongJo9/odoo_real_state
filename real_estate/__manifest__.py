{
    'name': "Real Estate",
    'version': '1.0',
    'depends': ['base','contacts'],
    'author': "Gerardo",
    'category': 'Category',
    'description': """,
    real estate module
    """,
    # data files always loaded at installation
    'data': [
        # 'views/mymodule_view.xml',
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_property_offer.xml',
        'views/estate_property_type_views.xml',
        'views/estate_property_tag.xml',
        'views/res_users_views.xml',
        'views/estate_property_inherit_view.xml',
        'views/menuitem.xml',
    ],
    'installable': True,
    "application": True,
        
    # data files containing optionally loaded demonstration data
    # 'demo': [
    #     'demo/demo_data.xml',
    # ],
}