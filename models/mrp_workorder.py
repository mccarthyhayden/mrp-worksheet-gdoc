from odoo import api, fields, models

class MrpRoutingWorkcenter(models.Model):
    _inherit = 'mrp.routing'

    worksheet_google_doc = fields.Char(
        'Worksheet URL', related='operation_id.worksheet_google_doc', readonly=True)