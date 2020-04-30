# -*- coding: utf-8 -*-
##*IMPORTS*##
from odoo import models, fields, api
from odoo.exceptions import ValidationError
#===================================================================================
##**CALLS MODEL**##
class Calls(models.Model):
    _name = 'iti.lab1.calls'
    _description = 'CDR'

    start_time = fields.Datetime()
    stop_time = fields.Datetime()
    duration = fields.Float(compute='_compute_duration',store=True)
    source = fields.Char()
    destination = fields.Char()
    name = fields.Char(default='New')
    station = fields.Many2one(comodel_name='iti.lab1.station')
    tags = fields.Many2many(comodel_name='iti.lab1.tags')
    state = fields.Selection([
        ('draft','Draft'),
        ('invoiced','Invoiced'),
    ] , default='draft' , string='Status')
    partner_id = fields.Many2one(comodel_name="res.partner")

    @api.constrains('stop_time')
    def check_stop_time(self):
        for rec in self:
            if rec.stop_time < rec.start_time:
                raise ValidationError('stop time can\'t be before start time!')

    @api.depends('start_time','stop_time')
    def _compute_duration(self):
        for rec in self:
            rec.duration = 0.0
            if rec.stop_time and rec.start_time:
                rec.duration = (rec.stop_time - rec.start_time).seconds / 60

    def create_invoice(self):
        invoice_obj = self.env['account.move'].create({
                'partner_id' : self.partner_id.id,
                'type' : 'out_invoice',
        })
        invoice_line_obj = self.env['account.move.line'].create({
            'name' : 'call cost',
            'move_id' : invoice_obj.id,
            'price_unit' : self.duration * 0.30,
            'account_id' : self.partner_id.property_account_receivable_id.id,
        })


#===================================================================================
##**STATION MODEL**##
class Station(models.Model):
    _name = 'iti.lab1.station'

    name = fields.Char()
    calls = fields.One2many(comodel_name='iti.lab1.calls',inverse_name='station')
#===================================================================================
##**TAGS MODEL**##
class Tags(models.Model):
    _name = 'iti.lab1.tags'

    name = fields.Char()