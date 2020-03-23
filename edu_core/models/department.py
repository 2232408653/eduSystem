# -*- coding: utf-8 -*-
from odoo import models, fields, api


class EduDepartment(models.Model):
    _name = "edu.department"
    _description = "院系"

    name = fields.Char('Name')
    code = fields.Char('Code')
    parent_id = fields.Many2one('edu.department', 'Parent Department')

    @api.model
    def create(self, vals):
        department = super(EduDepartment, self).create(vals)
        self.env.user.write({'department_ids': [(4, department.id)]})
        return department
