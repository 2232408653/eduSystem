# -*- coding: utf-8 -*-
from odoo import http

# class EduCore(http.Controller):
#     @http.route('/edu_core/edu_core/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/edu_core/edu_core/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('edu_core.listing', {
#             'root': '/edu_core/edu_core',
#             'objects': http.request.env['edu_core.edu_core'].search([]),
#         })

#     @http.route('/edu_core/edu_core/objects/<model("edu_core.edu_core"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('edu_core.object', {
#             'object': obj
#         })