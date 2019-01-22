# -*- coding: utf-8 -*-
from openerp import http

# class Vinyls(http.Controller):
#     @http.route('/vinyls/vinyls/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/vinyls/vinyls/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('vinyls.listing', {
#             'root': '/vinyls/vinyls',
#             'objects': http.request.env['vinyls.vinyls'].search([]),
#         })

#     @http.route('/vinyls/vinyls/objects/<model("vinyls.vinyls"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('vinyls.object', {
#             'object': obj
#         })