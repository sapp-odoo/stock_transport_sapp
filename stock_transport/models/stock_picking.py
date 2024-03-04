from odoo import fields, models, api

class StockPicking(models.Model):
    _name = "stock.picking"
    _inherit = "stock.picking"

    volume = fields.Integer(string="Volume", compute="_compute_volume")
