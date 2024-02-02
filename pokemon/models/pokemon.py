# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pokemon(models.Model):

    _name = 'pokemon.pokemon'
    _description = "Un pokemon concreto"

    nickname = fields.Char(string="Mote")
    trainer = fields.Many2one(comodel_name = "pokemon.trainer")
    
    specie = fields.Many2one(comodel_name = "pokemon.species", string="Especie", required=True)

    #ability = fields.Many2one(comodel_name = "pokemon.abilities", string = "Habilidad", related="specie.abilities")

    type_1 = fields.Many2one(comodel_name="pokemon.types",
                             string="Tipo 1",
                             related = "specie.type_1",
                             readonly = True,
                             store = False
                            )
    type_2 = fields.Many2one(comodel_name="pokemon.types",
                             string="Tipo 2",
                             related = "specie.type_2",
                             readonly = True,
                             store = False
                            )
    

    atk = fields.Integer(string = "Ataque",  required=True)
    hp = fields.Integer(string = "Puntos de Vida", required=True)
    defense = fields.Integer(string = "Defensa",  required=True)


    possible_State = [
        ("1", "Wild"),
        ("2", "Captured")
    ]

    

    #api depends de si tiene trainer entonces no es salvaje, sino capturado
    state = fields.Selection(possible_State, string = "Estado", required=True, default = "1")
    #state = fields.Char(string ="seleccion")


  
    @api.constrains('atk')
    def _compute_atk_change(self):
        for record in self:
            if record.atk > record.specie.atk:
                record.atk = record.specie.atk
            elif record.atk < 0:
                record.atk = 0
            
        
    @api.constrains('hp')
    def _compute_hp_change(self):
        for record in self:
            if record.hp > record.specie.hp:
                record.hp = record.specie.hp
            elif record.hp < 0:
                record.hp = 0

        
    @api.constrains('defense')
    def _compute_def_change(self):
        for record in self:

            if record.defense > record.specie.defense:
                record.defense = record.specie.defense
            elif record.defense < 0:
                record.defense = 0
   
    @api.constrains('trainer', 'state')
    def _check_max_pokemons(self):
        for record in self:
          #  if record.trainer and record.state == '2':  # Verificar si tiene entrenador y está capturado
                if len(record.trainer.team) > 6:
                    raise exceptions.ValidationError("Un entrenador no puede tener más de 6 pokemons.")