# -*- coding: utf-8 -*-

from odoo import models, fields


class cliente(models.Model):
    _name = 'taller.cliente'
    _description = 'Datos del cliente'


    name = fields.Char(string = "Nombre", required = True)
    surname  = fields.Char(string = "Apellidos", required = True)
    NIF = fields.Char(string = "DNI",required = True)
    phone = fields.Char(string = "Telefono", required=True)
    
