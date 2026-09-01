# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CarPolicy(models.Model):
    _name = 'car.policy'
    _description = 'Policy'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'effective_date desc'

    name = fields.Char(string='Policy Name', required=True, tracking=True)
    policy_type = fields.Char(string='Policy Type', tracking=True)
    version = fields.Char(string='Version', default='1.0', tracking=True)
    effective_date = fields.Date(string='Effective Date')
    review_date = fields.Date(string='Review Date')
    owner_id = fields.Many2one(
        'res.users',
        string='Owner',
        default=lambda self: self.env.user,
        tracking=True,
    )
    ai_compliance_gap = fields.Text(string='AI Compliance Gap')
    state = fields.Selection(
        [
            ('draft', 'Draft'),
            ('active', 'Active'),
            ('under_review', 'Under Review'),
            ('retired', 'Retired'),
        ],
        string='Status',
        default='draft',
        required=True,
        tracking=True,
    )
    content = fields.Html(string='Content')

    def action_set_active(self):
        self.write({'state': 'active'})

    def action_set_under_review(self):
        self.write({'state': 'under_review'})

    def action_set_retired(self):
        self.write({'state': 'retired'})
