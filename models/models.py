# -*- coding: utf-8 -*-

from openerp import models, fields, api

class estados(models.Model):
    _name = 'estados'
    _rec_name = "estado"

    estado = fields.Char(string="Estado de la orden de venta",)
    numero = fields.Integer(string="Numero del estado",)
    descripcion = fields.Text()

class sale_order(models.Model):
    _name = 'sale.order'
    _inherit = 'sale.order'

    estado_del_pedido = fields.Many2one(comodel_name="estados", string="Estado del pedido")

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         self.value2 = float(self.value) / 100
