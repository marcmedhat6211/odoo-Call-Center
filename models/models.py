# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Calls(models.Model):
    _name = 'iti.lab1.calls'
    _description = 'CDR'

    start_time = fields.Datetime()
    stop_time = fields.Datetime()
    duration = fields.Float(compute='_compute_duration',store=True)
    # duration = fields.Float(store=True)
    source = fields.Char()
    destination = fields.Char()
    name = fields.Char(default='New')

    @api.constrains('stop_time')
    def check_stop_time(self):
        for rec in self:
            if rec.stop_time < rec.start_time:
                raise ValidationError('stop time can\'t be before start time!')

    @api.depends('start_time','stop_time')
    def _compute_duration(self):
        for rec in self:
            rec.duration = (rec.stop_time - rec.start_time).seconds / 60