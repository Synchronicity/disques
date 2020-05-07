# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Pays(models.Model):
    _name = 'pays'
    _order = 'name'
    name = fields.Char(string='Pays',
                       required=True)