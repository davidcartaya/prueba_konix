# -*- coding: utf-8 -*-

from odoo import http
from odoo.http import request, Response
# from odoo.http import Controller, request, route
import json



class CustomerController(http.Controller):

    # Crear cliente
    @http.route('/create_customer', type='json', auth='user', methods=['POST'], csrf=False)
    def create_customer(self, **kwargs):
        datas = request.jsonrequest
        Partner = request.env['client.client']
        customer = Partner.create({
            'name': datas.get('name'),
            'last_name': datas.get('last_name'),
            'email': datas.get('email'),
            'phone': datas.get('phone')
        })
        return json.dumps({'message': f'Cliente {customer.name} creado con éxito'})

    # Editar cliente
    @http.route('/edit_customer', type='json', auth='none', methods=['POST'], csrf=False)
    def edit_customer(self, **post):
        datas = request.jsonrequest
        Partner = request.env['client.client']
        customer = Partner.browse(datas.get('client_id'))
        if not customer:
            return Response("Cliente no encontrado", status=404)
        customer.write({
            'name': datas.get('name') or customer.name,
            'last_name': datas.get('last_name') or customer.last_name,
            'email': datas.get('email') or customer.email,
            'phone': datas.get('phone') or customer.phone
        })
        return json.dumps({'message': f'Cliente {customer.name} modificado con éxito'})

    # Eliminar cliente
    @http.route('/delete_customer/<int:partner_id>', type='http', auth='none', methods=['POST'], csrf=False)
    def delete_customer(self, partner_id, **kwargs):
        Partner = request.env['client.client']
        customer = Partner.browse(partner_id)
        if not customer:
            return Response("Cliente no encontrado", status=404)
        customer.unlink()
        return json.dumps({'message': 'Cliente eliminado con éxito'})

