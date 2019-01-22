# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Artiste(models.Model):
    _name = 'vinyl.artiste'
    _order = 'name'
    name = fields.Char(string='Artiste / Groupe',
                       required=True)
    pays_id = fields.Many2one(comodel_name='vinyl.pays', string='Pays',
                              help="Nationalité de l'artiste")
    album_ids = fields.One2many(comodel_name='vinyl.vinyl', inverse_name='artiste_id', string='Album(s)',
                                required=True,
                                help="Album(s) de l'artiste")
