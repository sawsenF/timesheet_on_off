# -*- coding: utf-8 -*-

from openerp import models, fields, api
import datetime
import time
import logging
from openerp.exceptions import UserError, ValidationError
class timesheetmds(models.Model):
     _inherit = 'account.analytic.line'

     time_begin = fields.Float(string="Begin Time", store=True)
     time_end = fields.Float(string="End Time", store=True)
     state_on = fields.Integer(store=True)
     @api.one
     def confirm2 (self):
        sql1="select id from account_analytic_line where user_id= %d and state_on = 1" % (self.user_id)
        self.env.cr.execute(sql1)
        nb_true=self.env.cr.rowcount
        if nb_true>0:
            self.state_on=0
            if self.time_begin!=0:
                dt=time.time()
                self.time_end=dt
            else:
                self.time_end=0
            if self.time_end !=0:
                self.unit_amount  = float((self.unit_amount * 3600 + dt - self.time_begin)/3600)
                self.time_end=0
                self.time_begin=0
        else:
            self.state_on=1
            dt=time.time()
            self.time_begin=dt
        return True

     @api.one
     def confirm1 (self):
        sql1="select id from account_analytic_line where user_id= %d and state_on = 1" % (self.user_id)
        self.env.cr.execute(sql1)
        nb_true=self.env.cr.rowcount
        if nb_true<1:
            self.state_on=1
            dt=time.time()
            self.time_begin=dt