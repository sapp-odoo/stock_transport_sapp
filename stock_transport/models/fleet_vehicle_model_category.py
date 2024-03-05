from odoo import fields, models, api

class FleetVehicalModelCategory(models.Model):
    _name = "fleet.vehicle.model.category"
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Float(string="Max Weight")
    max_volume = fields.Float(string="Max Volume")

    @api.depends('name')
    def _compute_display_name(self):
        for record in self:
            value = super()._compute_display_name()
            for category in self:
                category.display_name = category.name + " (" + str(category.max_weight) + "kg, " + str(category.max_volume) + "m3)"
            return value
    