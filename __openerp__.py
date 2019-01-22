# -*- coding: utf-8 -*-
{
    'name': "vinyls",

    'summary': """
        Gestion des vinyls et des CD
        Albums - Genre - Artistes / Groupes""",

    'description': """
        Long description of module's purpose
    """,

    'author': "JLS_181120",
    'website': "http://192.168.56.101:8069",
    'application': True,

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/vinyl_views.xml',
        'views/vinyl_menu.xml',
        'views/artiste_views.xml',
    ],
}
