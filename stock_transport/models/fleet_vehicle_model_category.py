from odoo import fields, models, api

class FleetVehicalModelCategory(models.Model):
    _name = "fleet.vehicle.model.category"
    _inherit = "fleet.vehicle.model.category"

    max_weight = fields.Integer(string="Max Weight")
    max_volume = fields.Integer(string="Max Volume")

    @api.depends('max_weight', 'max_volume')
    def _compute_display_name(self):
        value = super()._compute_display_name()
        for category in self:
            category.display_name = category.name + " (" + str(category.max_weight) + "kg, " + str(category.max_volume) + "m3)"
        return value
