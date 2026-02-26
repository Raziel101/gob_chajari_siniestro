{
    'name': 'Registro de Siniestros de Vehiculos Municipal',
    'version': '19.0.1.0.0',
    'category': 'Custom',
    'summary': 'Registro de Siniestros de Vehiculos Municipal',
    'license': 'LGPL-3',
    'depends': ['base', 'mail'],
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'views/siniestro_views.xml',
        'views/persona_views.xml',
        'views/menu.xml',
    ],
    'installable': True,
    'application': True,
}
