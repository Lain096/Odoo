# -*- coding: utf-8 -*-

from odoo import models, fields, api


class normativa(models.Model):
    _name = 'taller.normativa'
    _description = 'Distintos tipos de normativa euro'

    meses = [
        ('ene', 'Enero'),
        ('feb', 'Febrero'),
        ('mar', 'Marzo'),
        ('abr', 'Abril'),
        ('may', 'Mayo'),
        ('jun', 'Junio'),
        ('jul', 'Julio'),
        ('ago', 'Agosto'),
        ('sep', 'Septiembre'),
        ('oct', 'Octubre'),
        ('nov', 'Noviembre'),
        ('dic', 'Diciembre'),
        ]


    name = fields.Char(string = "nombre", required=True) 

    year = fields.Integer(string = "año", required = True, default = 1900)
    month = fields.Selection(meses, string = "mes", required = True, default = 1900)