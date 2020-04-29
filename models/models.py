# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Calls(models.Model):
    _name = 'iti.lab1.calls'
    _description = 'CDR'
    # _rec_name = 'start_time'

    start_time = fields.Datetime()
    stop_time = fields.Datetime()
    duration = fields.Float()
    source = fields.Char()
    destination = fields.Char()
    name = fields.Char(default='New')