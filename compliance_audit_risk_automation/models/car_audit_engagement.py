# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CarAuditEngagement(models.Model):
    _name = 'car.audit.engagement'
    _description = 'Audit Engagement'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'start_date desc'

    name = fields.Char(string='Reference', required=True, tracking=True)
    audit_type = fields.Selection(
        [
            ('internal', 'Internal'),
            ('external', 'External'),
            ('regulatory', 'Regulatory'),
        ],
        string='Audit Type',
        default='internal',
        required=True,
        tracking=True,
    )
    scope = fields.Text(string='Scope')
    start_date = fields.Date(string='Start Date', tracking=True)
    end_date = fields.Date(string='End Date', tracking=True)
    auditor = fields.Char(string='Auditor')
    state = fields.Selection(
        [
            ('planned', 'Planned'),
            ('in_progress', 'In Progress'),
            ('review', 'Review'),
            ('completed', 'Completed'),
        ],
        string='Status',
        default='planned',
        required=True,
        tracking=True,
    )
    findings_count = fields.Integer(
        string='Findings Count',
        compute='_compute_findings_count',
        store=True,
    )
    ai_risk_assessment = fields.Text(string='AI Risk Assessment')

    @api.depends('state')
    def _compute_findings_count(self):
        for rec in self:
            rec.findings_count = 0

    def action_set_in_progress(self):
        self.write({'state': 'in_progress'})

    def action_set_review(self):
        self.write({'state': 'review'})

    def action_set_completed(self):
        self.write({'state': 'completed'})
