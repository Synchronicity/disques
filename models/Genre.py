# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Genre(models.Model):
    _name = 'genre'
    _order = 'name'
    name = fields.Char(string='Genre',
                       required=True)
