from datetime import date
from odoo import api, fields, models
from odoo.odoo import exceptions


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit=["mail.thread", "mail.activity.mixin"]
    _description = "hospital_patient"

    image = fields.Binary(string="Patient image")

    name = fields.Char(string='Name', required=True, translate=True, Tracking=True)
    ref = fields.Char(string='Reference', Tracking=True)
    date_of_birth = fields.Date(string='Date of birth')

    age = fields.Integer(string='Age', compute='_compute_age', Tracking=True)
    gender = fields.Selection([('male','Male'), ('female','Female')],string= 'Gender', Tracking=True)
    active = fields.Boolean(string='active', default=True)

    state = fields.Selection([('draft','draft'), ('confirm','Confirmed'),('done','Done'), ('cancel','Cancel')], default='draft', string='Status', Tracking=True)

    ## functions ##

    ## state functions ##
    def action_confirm(self):
        self.state = 'confirm'
    def action_done(self):
        self.state = 'done'
    def action_draft(self):
        self.state = 'draft'
    def action_cancel(self):
        self.state = 'cancel'
    ## end of state functions ##

    ## action functions ##
    ## end action functions ##

    ## dependant functions ##
    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth and record.date_of_birth.year < date.today().year:
                #tempAge = date.today().year - record.date_of_birth.year
                record.age = date.today().year - record.date_of_birth.year
            else:
                record.age = 0
    ## end dependant functions ##
    ## get functions ##
    def name_get(self):
        res = []
        for rec in self:
            name = "[" + str(rec.id) + "] " + rec.name
            res.append((rec.id,name))
        return res
    ## end get functions ##

    ## end functions ##
