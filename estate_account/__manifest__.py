{
    'name' : 'Estate Account',
    'version' : '1.0',
    'summary' : 'Integracion entre Estate y Account',
    'description' : 'Módulo de enlace entre el módulo Estate y el módulo Account.',
    'category' : 'Real Estate',
    'depends' : ['real_estate', 'account'],
    'data' : [
        # Aquí pondremos archivos XML de vistas en el futuro
    ],
    'installable' : True,
    'application' : False,
    'auto_install' : False,
}

#Con esto indicamos que el módulo solo se instalará si estate y account están presentes.