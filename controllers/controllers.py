# -*- coding: utf-8 -*-
# from odoo import http


# class CustomQuoteModule(http.Controller):
#     @http.route('/custom_quote_module/custom_quote_module/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/custom_quote_module/custom_quote_module/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('custom_quote_module.listing', {
#             'root': '/custom_quote_module/custom_quote_module',
#             'objects': http.request.env['custom_quote_module.custom_quote_module'].search([]),
#         })

#     @http.route('/custom_quote_module/custom_quote_module/objects/<model("custom_quote_module.custom_quote_module"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('custom_quote_module.object', {
#             'object': obj
#         })
