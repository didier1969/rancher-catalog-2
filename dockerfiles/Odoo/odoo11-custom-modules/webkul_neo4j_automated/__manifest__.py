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
{
  "name"                 :  "ODOO Neo4J Connector",
  "summary":  "This module will post data on Neo4j Graph Database.",
  "category"             :  "Tools",
  "version"              :  "1.0.1",
  "sequence"             :  1,
  "author"               :  "Webkul Software Pvt. Ltd.",
  "license"              :  "Other proprietary",
  "website"              :  "https://store.webkul.com/Odoo-Neo4j-Connector.html",
  "description"          :  """http://webkul.com/blog/odoo-neo4j-connector/""",
  "depends"              :  [
                             'base_automation',
                             'sale_management',
                            ],
  "data"                 :  [
                             'views/neo4j_automated_action.xml',
                             'views/res_config.xml',
                             'data/neo4j_server_data.xml',
                            ],
  "images"               :  ['static/description/Banner.png'],
  "application"          :  True,
  "installable"          :  True,
  "auto_install"         :  False,
  "price"                :  99,
  "currency"             :  "EUR",
  "pre_init_hook"        :  "pre_init_check",
  "external_dependencies":  {'python': ['py2neo']},
}