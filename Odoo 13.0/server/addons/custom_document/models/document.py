from odoo import models, fields

class CustomDocument(models.Model):
    _name = 'custom.document'
    _description = 'Custom Document'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    company_id = fields.Many2one('res.company', string='Company', required=True, default=lambda self: self.env.company)
    user_id = fields.Many2one('res.users', string='Created by', default=lambda self: self.env.user)
    assigned_employee_ids = fields.Many2many('hr.employee', string='Assigned Employees')
