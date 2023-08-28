# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'BR Addresses',
    'summary': 'Add extra fields on addresses',
    'sequence': '19',
    'complexity': 'easy',
    'description': """
BR Addresses
============

This module holds all extra fields one may need to manage accurately addresses in Brazil.
        """,
    'data': [
        'views/br_address.xml',
    ],
    'depends': ['base'],
    'license': 'LGPL-3',
}
