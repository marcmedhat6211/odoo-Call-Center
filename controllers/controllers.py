# -*- coding: utf-8 -*-
from odoo import http

# class OdooLab1(http.Controller):
#     @http.route('/odoo_lab1/odoo_lab1/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/odoo_lab1/odoo_lab1/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('odoo_lab1.listing', {
#             'root': '/odoo_lab1/odoo_lab1',
#             'objects': http.request.env['odoo_lab1.odoo_lab1'].search([]),
#         })

#     @http.route('/odoo_lab1/odoo_lab1/objects/<model("odoo_lab1.odoo_lab1"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('odoo_lab1.object', {
#             'object': obj
#         })