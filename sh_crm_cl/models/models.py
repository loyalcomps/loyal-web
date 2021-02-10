# -*- coding: utf-8 -*-

from odoo import fields, models, api


class CRMChecklist(models.Model):
    _name = "crm.checklist"
    _description = 'CRM Checklist'

    name = fields.Char("Name", required=True)
    description = fields.Char("Description")


class CalendarEvent(models.Model):
    _inherit = 'crm.lead'

    @api.depends('checklist_ids')
    def _compute_checklist(self):
        for rec in self:
            total_len = self.env['crm.checklist'].search_count([])
            check_list_len = len(rec.checklist_ids)
            if total_len != 0:
                rec.checklist = (check_list_len * 100) / total_len
        # self.ensure_one()
        #
        # total_cnt = self.env['crm.checklist'].sudo().search_count([])
        # comp_cnt = 0
        #
        # for rec in self.sudo().checklist_ids:
        #
        #     if rec.name:
        #         comp_cnt += 1
        #
        # if total_cnt > 0:
        #     self.checklist = (100.0 * comp_cnt) / total_cnt
        # else:
        #     self.checklist = 0

    checklist_ids = fields.Many2many("crm.checklist", string="Checklist")
    checklist = fields.Float(string="Checklist Completed", compute="_compute_checklist", store=True, recompute=True,
                                      default=0.0)

