# -*- coding: utf-8 -*-
from openerp import http

# class EstadosVenta(http.Controller):
#     @http.route('/estados_venta/estados_venta/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/estados_venta/estados_venta/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('estados_venta.listing', {
#             'root': '/estados_venta/estados_venta',
#             'objects': http.request.env['estados_venta.estados_venta'].search([]),
#         })

#     @http.route('/estados_venta/estados_venta/objects/<model("estados_venta.estados_venta"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('estados_venta.object', {
#             'object': obj
#         })