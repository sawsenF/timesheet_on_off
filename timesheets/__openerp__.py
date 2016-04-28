# -*- coding: utf-8 -*-
{
    'name': "timesheet on/off button time",

    'summary': """
       launch the timer in one click . Just choose your task and switch it on, Only one task can be active in the same time """,

    'description': """
        Long description of module's purpose
    """,

    'author': "Sawsen Fattahi",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_timesheet','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    'css': [
        'static/css/css.css',
    ],

    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}