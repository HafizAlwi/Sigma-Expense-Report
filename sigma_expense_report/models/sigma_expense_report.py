from odoo import api, models
from datetime import datetime

class SigmaExpenseReport(models.AbstractModel):
    _name = 'report.sigma_expense_report.sigma_expense_report'
    _description = 'Sigma Expense Report'
    _inherit = 'hr.expense.sheet'

    @api.model
    def get_report_values(self, docids, data=None):
        expenses = self.env['hr.expense.sheet'].browse(docids)
        return {
            'doc_ids': docids,
            'doc_model': 'hr.expense.sheet',
            'docs': expenses,
        }

    #def action_generate_report(self):
    #    context = self.env.context.copy()
    #    context.update = ({
    #        'employee_id': self.employee_id.name,
    #    })
    #    return self.env.ref('report.sigma_expense_report.sigma_expense_report').report_action(self, data=None, config=False, context=context)