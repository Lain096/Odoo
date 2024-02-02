# -*- coding: utf-8 -*-

from odoo import models, fields

class certificado(models.Model):
    _name = 'taller.certificado'
    _description = 'Datos del certificado de emisiones'

    name = fields.Char(string = "Nombre", required = True)
    image_url = fields.Char(string = "Logo")
    