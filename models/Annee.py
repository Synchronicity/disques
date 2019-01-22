# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Genre(models.Model):
    _name = 'vinyl.annee'
    _order = 'name'
    name = fields.Char(string='Année',
                       required=True)
