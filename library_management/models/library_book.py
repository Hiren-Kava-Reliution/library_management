from odoo import fields, models

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Book Name')
    author = fields.Char(string='Author')
    available_qty = fields.Integer(string='Available Quantity')
    is_available = fields.Boolean(string='Is Available')