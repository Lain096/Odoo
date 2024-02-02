# -*- coding: utf-8 -*-

from odoo import models, fields

class modelo(models.Model):
    _name = 'taller.modelo'
    _description = 'Datos del modelo de la marca'

    modelo = fields.Char(string = "Modelo", required = True)
    brand = fields.Many2one(comodel_name = "taller.marca", string = "Marca", required = True)
    