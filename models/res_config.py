# -*- coding: utf-8 -*-
from openerp.models import TransientModel
from openerp import fields


class WebsiteConfigSettings(TransientModel):

    """Adds the fields for CrazyEgg."""

    _inherit = 'website.config.settings'

    crazyegg = fields.Boolean(
        string='Use CrazyEgg',
        related='website_id.crazyegg',
        help=('if activated CrazyEgg tracking is active')
    )
    crazyegg_script = fields.Text(
        string='CrazyEgg Script',
        related='website_id.crazyegg_script'
    )
