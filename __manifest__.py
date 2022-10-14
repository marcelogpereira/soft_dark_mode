# -*- coding: utf-8 -*-

{
    'name': 'Soft Dark Mode',
    'category': 'Hidden',
    'version': '1.0',
    'description': """ """,
    'depends': ['web_enterprise'],
    'author': "Arxi",
    'auto_install': True,
    'data': [
    ],
    'assets': {

#         ========= Dark Mode =========
        "web.dark_mode_variables": [
            # web._assets_primary_variables
            ('before', 'web_enterprise/static/src/scss/primary_variables.dark.scss', 'soft_dark_mode/static/src/scss/primary_variables.dark.scss'),
        ],
         "web.dark_mode_assets_backend": [
            # assets_backend
            'soft_dark_mode/static/src/**/**/*.dark.scss',
        ],

    },
    'license': 'OPL-1',
}
