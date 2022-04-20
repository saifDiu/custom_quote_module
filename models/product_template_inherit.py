from odoo import models, api, fields, _


class ProductTemplateInherit(models.Model):
    _inherit = 'product.template'

    height = fields.Float(string="Height")
    width = fields.Float(string="Width")

