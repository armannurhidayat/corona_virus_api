# -*- coding: utf-8 -*-
{
    'name': "api corona virus",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Corona Virus API
	special thanks to https://services1.arcgis.com
    """,

    'author': "Arman Nur Hidayat",
    'website': "https://github.com/armannurhidayat",


    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/squence.xml',
        'views/views.xml',
    ],
}
