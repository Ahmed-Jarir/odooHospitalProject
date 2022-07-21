# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Hospital Management',
    'version': '0.0.1',
    'category': 'hospital',
    'author': 'Ahmed Jarir',
    'sequence': -100,
    'summary': 'hospital management system',
    'description': """
    hospital management system
    """,
    'depends': ["mail"],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/male_patient_view.xml',
        'views/appointment_wizard_view.xml',
        'views/appointment_view.xml',

    ],
    'demo': [
    ],
    'application': True,
    'installable': True,
    'auto_install': False,
    'assets': {
    },
    'license': 'LGPL-3',
}
