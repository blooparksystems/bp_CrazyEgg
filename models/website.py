 # -*- coding: utf-8 -*-
from openerp.models import Model
from openerp import fields

class Website(Model):
    _inherit = 'website'

    crazyegg = fields.Boolean(
        string='Use CrazyEgg',
        default=False,
        help=('if activated CrazyEgg tracking is active')
    )
