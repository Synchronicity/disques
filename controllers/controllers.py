# -*- coding: utf-8 -*-
from openerp import http

# class disques(http.Controller):
#     @http.route('/disques/disques/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/disques/disques/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('disques.listing', {
#             'root': '/disques/disques',
#             'objects': http.request.env['disques.disques'].search([]),
#         })

#     @http.route('/disques/disques/objects/<model("disques.disques"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('disques.object', {
#             'object': obj
#         })
