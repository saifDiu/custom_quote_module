from odoo import models,api,fields,_


class SaleOrderInherit(models.Model):
    _inherit = 'sale.order.line'

    height_prod = fields.Float(string="Alto")
    width_prod = fields.Float(string="Ancho")
    mando = fields.Text(string="mando")
    motor = fields.Boolean(string="motor")
    encajonda = fields.Boolean(string="Encajonada")

    product_uom_qty = fields.Float(string='m2', digits='Product Unit of Measure', required=True, default=0.0)

    @api.onchange('height_prod','width_prod')
    def onchange_height_width(self):
        for rec in self:
            if rec.height_prod and rec.width_prod:
                rec.product_uom_qty = rec.height_prod * rec.width_prod

