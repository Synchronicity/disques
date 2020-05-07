# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Disque(models.Model):
    _name = 'disque'
    _order = 'name'
    name = fields.Char(string='Album',
                       required=True,
                       help="Titre de l'album")
    genre_id = fields.Many2many(comodel_name='genre', string='Genre',
                                required=True,
                                help="Genre de l'album")
    artiste_id = fields.Many2one(comodel_name='artiste', string="Artiste / Groupe",
                                 required=True,
                                 help="Artiste de l'album")
    annee = fields.Many2one(comodel_name='annee', string='Année',
                            help="Année de sortie de l'album")
    pays_id = fields.Many2one(comodel_name='pays', string='Pays',
                              related="artiste_id.pays_id",
                              help="Nationalité de l'artiste")
    support = fields.Selection([('0', 'CD'), ('1', 'Vinyl'), ('2', 'CD et Vinyl')], 'Support')
