# -*- coding: utf-8 -*-
from openerp import http

# class Timesheetmds(http.Controller):
#     @http.route('/timesheetmds/timesheetmds/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/timesheetmds/timesheetmds/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('timesheetmds.listing', {
#             'root': '/timesheetmds/timesheetmds',
#             'objects': http.request.env['timesheetmds.timesheetmds'].search([]),
#         })

#     @http.route('/timesheetmds/timesheetmds/objects/<model("timesheetmds.timesheetmds"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('timesheetmds.object', {
#             'object': obj
#         })