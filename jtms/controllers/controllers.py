# -*- coding: utf-8 -*-
# from odoo import http


# class Jtms(http.Controller):
#     @http.route('/jtms/jtms/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/jtms/jtms/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('jtms.listing', {
#             'root': '/jtms/jtms',
#             'objects': http.request.env['jtms.jtms'].search([]),
#         })

#     @http.route('/jtms/jtms/objects/<model("jtms.jtms"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('jtms.object', {
#             'object': obj
#         })
