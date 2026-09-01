# -*- coding: utf-8 -*-
from odoo import api, fields, models


class CarRiskRegister(models.Model):
    _name = 'car.risk.register'
    _description = 'Risk Register'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _order = 'risk_score desc'

    name = fields.Char(string='Risk Title', required=True, tracking=True)
    risk_category = fields.Selection(
        [
            ('financial', 'Financial'),
            ('operational', 'Operational'),
            ('strategic', 'Strategic'),
            ('compliance', 'Compliance'),
            ('cyber', 'Cyber'),
        ],
        string='Risk Category',
        default='operational',
        required=True,
        tracking=True,
    )
    likelihood = fields.Integer(
        string='Likelihood (1-5)',
        default=3,
        tracking=True,
    )
    impact = fields.Integer(
        string='Impact (1-5)',
        default=3,
        tracking=True,
    )
    risk_score = fields.Float(
        string='Risk Score',
        compute='_compute_risk_score',
        store=True,
    )
    ai_mitigation_priority = fields.Text(string='AI Mitigation Priority')
    mitigation_plan = fields.Text(string='Mitigation Plan')
    owner_id = fields.Many2one(
        'res.users',
        string='Owner',
        default=lambda self: self.env.user,
        tracking=True,
    )
    state = fields.Selection(
        [
            ('identified', 'Identified'),
            ('assessed', 'Assessed'),
            ('mitigating', 'Mitigating'),
            ('monitored', 'Monitored'),
            ('closed', 'Closed'),
        ],
        string='Status',
        default='identified',
        required=True,
        tracking=True,
    )

    @api.depends('likelihood', 'impact')
    def _compute_risk_score(self):
        for rec in self:
            rec.risk_score = (rec.likelihood or 0) * (rec.impact or 0)

    def action_set_assessed(self):
        self.write({'state': 'assessed'})

    def action_set_mitigating(self):
        self.write({'state': 'mitigating'})

    def action_set_monitored(self):
        self.write({'state': 'monitored'})

    def action_set_closed(self):
        self.write({'state': 'closed'})
