# -*- coding: utf-8 -*-

from odoo import models, fields

class marca(models.Model):
    _name = 'taller.marca'
    _description = 'Datos de la marca'

    name = fields.Char(string = "Marca", required = True)
    image_url = fields.Char(string = "Logo")