# -*- coding: utf-8 -*-
##############################################################################
#
# Odoo, an open source suite of business apps
# This module copyright (C) 2015 bloopark systems (<http://bloopark.de>).
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': "CrazyEgg",

    'summary': """
        CrazyEgg Tracking""",

    'description': """
         CrazyEgg Tracking""",

    'author': "bloopark systems GmbH & Co. KG",
    'website': "http://www.bloopark.de",

    'category': 'Tracking',
    'version': '1.0',

    'depends': [
        'base',
        'website_sale'
    ],
    'data': [
        'views/templates.xml',
        'views/website_views.xml',
        'views/res_config.xml'
    ],

    'demo': [
    ],

    'tests': [
    ],
}
