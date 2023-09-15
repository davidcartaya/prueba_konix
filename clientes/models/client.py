from odoo import api, fields, models, _

class Client(models.Model):
    _name = 'client.client'

    name = fields.Char(string="Nombre")
    last_name = fields.Char(string="Apellidos")
    email = fields.Char(string="Email")
    phone = fields.Char(string="Número de teléfono")