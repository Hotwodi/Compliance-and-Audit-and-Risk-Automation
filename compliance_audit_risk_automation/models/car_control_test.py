# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CarControlTest(models.Model):
    _name = 'car.control.test'
    _description = 'Control Test'
    _inherit = ['mail.thread']
    _order = 'test_date desc'

    name = fields.Char(string='Test Name', required=True, tracking=True)
    control_id = fields.Char(string='Control ID', tracking=True)
    test_type = fields.Selection(
        [
            ('automated', 'Automated'),
            ('manual', 'Manual'),
            ('sample', 'Sample'),
        ],
        string='Test Type',
        default='manual',
        required=True,
        tracking=True,
    )
    sample_size = fields.Integer(string='Sample Size', default=0)
    passed = fields.Integer(string='Passed', default=0)
    failed = fields.Integer(string='Failed', default=0)
    test_date = fields.Date(string='Test Date', default=fields.Date.context_today)
    ai_automation_potential = fields.Text(string='AI Automation Potential')
    result = fields.Selection(
        [
            ('pass', 'Pass'),
            ('fail', 'Fail'),
            ('exception', 'Exception'),
        ],
        string='Result',
        default='pass',
        tracking=True,
    )
    notes = fields.Text(string='Notes')
