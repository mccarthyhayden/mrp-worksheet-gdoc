from odoo import api, fields, models

class MrpRoutingWorkcenter(models.Model):
    _inherit = 'mrp.routing'

    worksheet_type = fields.Selection([
        ('pdf', 'PDF'), ('google_slide', 'Google Slide'), ('google_doc', 'Google Doc'), ('text', 'Text')],
        string="Work Sheet", default="text",
        help="Defines if you want to use a PDF, Google Slide, or Google Doc as a work sheet."
    )
    worksheet_google_doc = fields.char('Google Doc', help="Paste the url of your Google Doc. Make sure the access to the document is public.")