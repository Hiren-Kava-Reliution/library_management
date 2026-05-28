from odoo import fields, models, api

class LibraryBookIssue(models.Model):
    _name = 'library.book.issue'
    _description = 'Library Book Issue'

    book_id = fields.Many2one('library.book', string='Book',  domain="[('available_qty', '>', 0)]")
    member_id = fields.Many2one('library.member', string='Member', domain=[('is_active', '=', True)])
    issue_date = fields.Date(string='Date of Issue', default=fields.Date.today())
    return_date = fields.Date(string='Date of Return')
    status = fields.Selection(selection=[('draft', 'Draft'), ('issued', 'Issued'), ('returned', 'Returned')], default='draft')
    days_issued = fields.Integer(string='Days Issued', compute="compute_days_calculate")

    api.depends('issue_date', 'return_date')
    def compute_days_calculate(self):
        for record in self:
            if record.issue_date and record.return_date:
                delta = record.return_date - record.issue_date
                record.days_issued = delta.days

            else:
                record.days_issued = 0