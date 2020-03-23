# -*- coding: utf-8 -*-
{
    'name': "edu_core",

    'summary': """
        管理学生,院系和教育学院""",

    'description': """
        基础开发模块,其余所有功能都由此开发
    """,

    'author': "DingShuo",
    'website': "http://www.odoo12.xyz",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/12.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Edu',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['board', 'document', 'hr', 'web', 'website'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/department_view.xml',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}