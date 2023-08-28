# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, models


class Company(models.Model):
    _inherit = 'res.company'

    street_number = fields.Char('Número')
    district = fields.Char('Bairro')
