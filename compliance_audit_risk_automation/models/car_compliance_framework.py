# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CarComplianceFramework(models.Model):
    _name = 'car.compliance.framework'
    _description = 'Compliance Framework'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'name'

    name = fields.Char(string='Name', required=True, tracking=True)
    framework = fields.Selection(
        [
            ('sox', 'SOX'),
            ('gdpr', 'GDPR'),
            ('hipaa', 'HIPAA'),
            ('iso27001', 'ISO 27001'),
            ('pci_dss', 'PCI DSS'),
            ('custom', 'Custom'),
        ],
        string='Framework',
        default='custom',
        required=True,
        tracking=True,
    )
    description = fields.Text(string='Description')
    owner_id = fields.Many2one(
        'res.users',
        string='Owner',
        default=lambda self: self.env.user,
        tracking=True,
    )
    last_assessment = fields.Date(string='Last Assessment')
    next_assessment = fields.Date(string='Next Assessment')
    compliance_score = fields.Float(
        string='Compliance Score',
        default=0.0,
        tracking=True,
    )
    state = fields.Selection(
        [
            ('compliant', 'Compliant'),
            ('partial', 'Partial'),
            ('non_compliant', 'Non-Compliant'),
        ],
        string='Status',
        default='partial',
        required=True,
        tracking=True,
    )

    def action_set_compliant(self):
        self.write({'state': 'compliant'})

    def action_set_partial(self):
        self.write({'state': 'partial'})

    def action_set_non_compliant(self):
        self.write({'state': 'non_compliant'})
