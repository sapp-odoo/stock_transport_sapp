from odoo import fields, models, api

class StockPickingBatch(models.Model):
    _name = "stock.picking.batch"
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one("dock", string="Dock")
    vehicle_id = fields.Many2one("fleet.vehicle", string="Vehicle")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category", string="Vehicle Category")
    weight = fields.Integer(string="Weight", compute="_compute_weight", store=True)
    volume = fields.Integer(string="Volume", compute="_compute_volume", store=True)

    @api.depends('vehicle_category_id', 'move_line_ids')
    def _compute_weight(self):
        counted_weight = 0
        for transfers in self.move_line_ids:
            counted_weight = counted_weight + (transfers.product_id.product_tmpl_id.weight) * (transfers.quantity)
        if(self.vehicle_category_id.max_weight!=0):
            self.weight = round(100.0 * counted_weight / self.vehicle_category_id.max_weight)
        else:
            self.weight = 0
    
    @api.depends('vehicle_category_id', 'move_line_ids')
    def _compute_volume(self):
        counted_volume = 0
        for transfers in self.move_line_ids:
            counted_volume = counted_volume + (transfers.product_id.product_tmpl_id.volume) * (transfers.quantity)
        if(self.vehicle_category_id.max_volume!=0):
            self.volume = round(100.0 * counted_volume / self.vehicle_category_id.max_volume)
        else:
            self.volume = 0
