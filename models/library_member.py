from odoo import fields, models

class LibraryMember(models.Model):
    _name = 'library.member'
    _description = 'Library Member'

    name = fields.Char(string='Member Name')
    email = fields.Char(string='Email Address')
    is_active = fields.Boolean()