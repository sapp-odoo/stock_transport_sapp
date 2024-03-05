from odoo import fields, models, api

class StockPickingBatch(models.Model):
    _name = "stock.picking.batch"
    _inherit = "stock.picking.batch"

    dock_id = fields.Many2one("dock", string="Dock")
    vehicle_id = fields.Many2one("fleet.vehicle", string="Vehicle")
    vehicle_category_id = fields.Many2one("fleet.vehicle.model.category", readonly=False, related="vehicle_id.category_id", string="Vehicle Category", store=True)
    weight = fields.Float(string="Weight", compute="_compute_weight", store=True)
    volume = fields.Float(string="Volume", compute="_compute_volume", store=True)
    weight_progress = fields.Float(compute="_compute_weight")
    volume_progress = fields.Float(compute="_compute_volume")
    transfers_count = fields.Integer(string="Transfers", compute="_compute_transfers_count", store=True)
    lines_count = fields.Integer(string="Lines", compute="_compute_lines_count", store=True)

    @api.depends('vehicle_category_id', 'move_line_ids')
    def _compute_weight(self):
        for record in self:
            counted_weight = 0
            for transfers in record.move_line_ids:
                counted_weight = counted_weight + (transfers.product_id.product_tmpl_id.weight) * (transfers.quantity)
            record.weight = counted_weight
            if(record.vehicle_category_id.max_weight!=0):
                record.weight_progress = round(100.0 * counted_weight / record.vehicle_category_id.max_weight)
            else:
                record.weight_progress = 0
    
    @api.depends('vehicle_category_id', 'move_line_ids')
    def _compute_volume(self):
        for record in self:
            counted_volume = 0
            for transfers in record.move_line_ids:
                counted_volume = counted_volume + ((transfers.product_id.product_tmpl_id.volume) * (transfers.quantity))
            record.volume = counted_volume
            if(record.vehicle_category_id.max_volume!=0):
                record.volume_progress = round(100.0 * counted_volume / record.vehicle_category_id.max_volume)
            else:
                record.volume_progress = 0

    @api.depends('name')
    def _compute_display_name(self):
        value = super()._compute_display_name()
        for category in self:
            category.display_name = category.name + ": " + str(category.weight) + "kg, " + str(category.volume) + "m3"
        return value

    @api.depends('picking_ids')
    def _compute_transfers_count(self):
        for record in self:
            record.transfers_count = len(record.picking_ids)

    @api.depends('move_line_ids')
    def _compute_lines_count(self):
        for record in self:
            record.lines_count = len(record.move_line_ids)

