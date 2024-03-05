from odoo import fields, models, api

class StockPicking(models.Model):
    _name = "stock.picking"
    _inherit = "stock.picking"

    volume = fields.Float(string="Volume", compute="_compute_volume")

    @api.depends('name', 'move_ids')
    def _compute_volume(self):
        for record in self:
            counted_volume = 0
            for transfers in record.move_ids:
                counted_volume = counted_volume + (transfers.product_id.product_tmpl_id.volume) * (transfers.quantity)
            record.volume = counted_volume
