 # -*- coding: utf-8 -*-
from openerp.models import TransientModel
from openerp import fields

class WebsiteConfigSettings(TransientModel):
    _inherit = 'website.config.settings'

    crazyegg = fields.Boolean(
        string='Use CrazyEgg',
        related='website_id.crazyegg',
        help=('if activated CrazyEgg tracking is active')
    )
