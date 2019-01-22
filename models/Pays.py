# -*- coding: utf-8 -*-
from openerp import models, fields, api


class Pays(models.Model):
    _name = 'vinyl.pays'
    _order = 'name'
    name = fields.Char(string='Pays',
                       required=True)