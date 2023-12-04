from odoo import models, fields

class DocumentFilterWizard(models.TransientModel):
    _name = 'document.filter.wizard'
    _description = 'Document Filter Wizard'

    date_from = fields.Date(string='Date From')
    date_to = fields.Date(string='Date To')
    employee_ids = fields.Many2many('hr.employee', string='Select Employee')

    def filter_documents(self):
        domain = []

        if self.date_from:
            domain.append(('create_date', '>=', self.date_from))
        if self.date_to:
            domain.append(('create_date', '<=', self.date_to))
        if self.employee_ids:
            domain.append(('assigned_employee_ids', 'in', self.employee_ids.ids))

        documents = self.env['custom.document'].search(domain)
        return {
            'name': 'Filtered Documents',
            'view_mode': 'tree,form',
            'res_model': 'custom.document',
            'view_id': False,
            'type': 'ir.actions.act_window',
            'domain': [('id', 'in', documents.ids)],
        }
