# copyright 2022 Sodexis
# license OPL-1 (see license file for full copyright and licensing details).

from odoo import models,fields


class ProductProduct(models.Model):
    _inherit = "product.product"


    notes = fields.Html(string='Notes')
