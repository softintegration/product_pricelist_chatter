# -*- coding: utf-8 -*- 

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class Pricelist(models.Model):
    _name = "product.pricelist"
    _inherit = ['mail.thread', 'mail.activity.mixin', 'product.pricelist']



