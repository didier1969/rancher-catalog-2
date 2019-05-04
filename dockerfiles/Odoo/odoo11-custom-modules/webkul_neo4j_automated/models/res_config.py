# -*- coding: utf-8 -*-
#################################################################################
# Author      : Webkul Software Pvt. Ltd. (<https://webkul.com/>)
# Copyright(c): 2015-Present Webkul Software Pvt. Ltd.
# All Rights Reserved.
#
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://store.webkul.com/license.html/>
#################################################################################

import re
import odoo
from odoo import api, fields, models, _
from odoo.exceptions import UserError

class OdooNeo4jConfig(models.Model):
    _name = "odoo.neo4j.config"
    _description = "Neo4j Configuration"



    url = fields.Char(string='Base URL', required=True, copy=False)
    port = fields.Char(string='Bolt Port', default="7687", required=True, copy=False)
    name = fields.Char(string='Name', required=True, copy=False)
    active = fields.Boolean(string="Active", default=True, copy=False)
    cypher_text = fields.Char(string="Cypher Code",copy=False)
    username = fields.Char(string="User Name", required=True, copy=False)
    password = fields.Char(string="Password", required=True, copy=False)

    @api.model
    def create(self, vals):
        active_ids = self.search([('active', '=', True)])
        if vals['active'] and active_ids:
            raise UserError(
                _('Warning!\nSorry, Only one active connection is allowed.'))
        return super(OdooNeo4jConfig, self).create(vals)

    @api.multi
    def write(self, vals):
        active_ids = self.search([('active', '=', True)])
        if vals:
            if len(active_ids) > 0 and 'active' in vals and vals['active']:
                raise UserError(
                    _('Warning!\nSorry, Only one active connection is allowed.'))
        return super(OdooNeo4jConfig, self).write(vals)
