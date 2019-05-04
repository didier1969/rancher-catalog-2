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

import logging
_logger = logging.getLogger(__name__)
try:
    from py2neo import Graph
except Exception as e:
    _logger.error("#WKDEBUG-1  python  py2neo library not installed .")


import requests

try: import simplejson as json
except ImportError: import json

from odoo import api, fields, models, _
from odoo.exceptions import UserError, ValidationError


class BaseAutomation(models.Model):

    _inherit = 'base.automation'

    query = fields.Text(string="Neo4j Query")
    field_ids = fields.Many2many('wk.fields.mapping', 'rule_action_field_mapping', 'rule_id','object_id', 'Field Mappings')
    is_neo4j = fields.Boolean(string="Neo4j", default=False)

    def create_connection(self):
        try:
            connection_obj = self.env["odoo.neo4j.config"].search([('active','=',True)],limit=1)
            if connection_obj:
                url = connection_obj.url
                port = connection_obj.port
                uname = connection_obj.username
                pwd = connection_obj.password
                session = Graph(url=url, port=port, user=uname, password=pwd)
                return session
            raise UserError(_("Neo4j Connection Not Found..!!"))
        except Exception as e:
            raise UserError(e)

    @api.model
    def execute_query(self,_object):
        for record in self.search([('query','!=',None),('model_id','=',self._context.get('active_model'))]):
            session = record.create_connection()
            query = record.query
            params = {}
            for fields in record.field_ids:
                field_name = str(fields.field1_name)
                order_list = _object.read()
                for order in order_list:
                    if isinstance(order.get(field_name), int) or isinstance(order.get(field_name), bool) or isinstance(order.get(field_name), str) or isinstance(order.get(field_name), float) :
                        params[fields.field2_name] = order.get(field_name)
                    elif isinstance(order.get(field_name), tuple) : 
                        params[fields.field2_name] = str(order.get(field_name)[1])
            result = session.run(query,params)
        return result

class WkFieldsMapping(models.Model):
    
    _name = 'wk.fields.mapping'

    field1_name = fields.Char(string="Odoo Field", required=True)
    field2_name = fields.Char(string="Neo4j Field", required=True)

class SaleOrderLine(models.Model):
    
    _inherit = "sale.order.line"

    partner_id = fields.Many2one(related='order_id.partner_id', string="Customer Name")
        
