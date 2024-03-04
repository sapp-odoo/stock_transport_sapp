from odoo import fields, models, api

class Dock(models.Model):
    _name = "dock"

    name = fields.Char(string="Dock")
