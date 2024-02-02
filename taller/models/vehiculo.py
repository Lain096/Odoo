# -*- coding: utf-8 -*-

from odoo import models, fields, api

class vehiculo(models.Model):
    _name = 'taller.vehiculo'
    _description = 'Descripcion general del vehiculo'


    matricula = fields.Char(string = "Matricula", required = True)
    n_bastidor = fields.Char(string = "Numero de bastidor", required = True)
    marca = fields.Many2one(comodel_name = "taller.marca", string = "Marca", required = True)
    cliente = fields.Many2one(comodel_name = "taller.cliente", string = "Dueño", required = True)
   
    modelo = fields.Many2one(comodel_name = "taller.modelo" ,string = "Modelo", required = True)
    date = fields.Integer(string = "Year", required = True)
    image = fields.Image(string = "Imagen")
    opcion_combustible = [("d", "Diesel"), ("g", "Gasolina"), ("e", "Electrico")]
    combustible = fields.Selection(opcion_combustible, string = "Combustible", required = True)
    
    cc = fields.Integer(string = "Cilindradas")
    kv = fields.Float(string = "Caballos de vapor")
    #kw = fields.Integer(string = "KiloWatts")
    color = fields.Char(string = "Color")

    t_veh = [
        ('co', 'Coche'),
        ('cama', 'Camioneta'),
        ('suv', 'SUV'),
        ('moto', 'Motocicleta'),
        ('bici', 'Bicicleta'),
        ('camo', 'Camion'),
        ('bus', 'Autobus'),
        ('furgo', 'Furgoneta'),
    ]

    tipo_vehiculo = fields.Selection(t_veh, string = "Tipo de Vehiculo", required = True)
    description = fields.Text(string= "Descripcion", required = True)

    _sql_constraints = [
            ('matricula_unique', 'UNIQUE(matricula)', 'El número de matrícula deberá ser único.')
        ]


    @api.constrains('matricula')
    def _check_unique_matricula(self):
        for vehiculo in self:
            if vehiculo.matricula:
                duplicate_matricula = self.search([('id', '!=', vehiculo.id), ('matricula', '=', vehiculo.matricula)])
                if duplicate_matricula:
                    raise ValidationError("La matrícula debe ser única")

    @api.depends('cc')
    def _compute_calculate_kv(self):
        self.kv = (self.cc * 0.08)
    


   