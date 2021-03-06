# -*- coding: utf-8 -*-
{
    'name': "service_desk",

    'summary': """
        Mesa de servicios adaptado para la Universidad Andina Simón Bolívar""",

    'description': """
        Mesa de servicios adaptado para la Universidad Andina Simón Bolívar
    """,

    'author': "Carlos Díaz",
    'website': "http://www.uasb.edu.ec",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Project',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['project', 'project_issue'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/project_issue.xml',
        'views/website_project_issue.xml',
        'views/project_issue_workflow.xml',
        'views/website_project_detail_ticket.xml',
        'views/website_project_create_ticket.xml',
        'views/website_project_create_ticket_out.xml',
        'views/project_user.xml',

    ],
}