# -*- coding: utf-8 -*-
{
    'name': 'Compliance, Audit & Risk Automation',
    'version': '18.0.1.0.0',
    'summary': 'AI-powered compliance, audit, and risk management automation',
    'description': """
Compliance, Audit & Risk Automation
===================================
Manage audit engagements, compliance frameworks, risk registers,
control testing, and policy management with AI-assisted insights.
""",
    'author': 'SoftaiDev',
    'website': 'https://softaidev.pages.dev',
    'category': 'Productivity/AI',
    'license': 'LGPL-3',
    'price': 899.99,
    'currency': 'USD',
    'application': True,
    'installable': True,
    'depends': ['base', 'web', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/car_audit_engagement_views.xml',
        'views/car_compliance_framework_views.xml',
        'views/car_risk_register_views.xml',
        'views/car_control_test_views.xml',
        'views/car_policy_views.xml',
        'views/car_menu.xml',
    ],
    'assets': {},
}
