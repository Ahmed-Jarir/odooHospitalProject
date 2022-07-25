from datetime import date
from odoo import api, fields, models
from odoo.exceptions import ValidationError


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ["mail.thread", "mail.activity.mixin"]
    _description = "hospital_patient"

    image = fields.Binary(string="Patient image")

    name = fields.Char(string='Name', required=True, translate=True, Tracking=True)
    ref = fields.Many2one("hospital.doctors", string="reference", required=True)
    date_of_birth = fields.Date(string='Date of birth')

    age = fields.Integer(string='Age', compute='_compute_age', Tracking=True, store=True)
    gender = fields.Selection([('male','Male'), ('female','Female')],string= 'Gender', Tracking=True)
    active = fields.Boolean(string='active', default=True)

    state = fields.Selection([('draft', 'draft'), ('confirm', 'Confirmed'), ('done', 'Done'), ('cancel', 'Cancel')], default='draft', string='Status', Tracking=True)

    appointment_ids = fields.One2many('hospital.appointment', 'patient_id', string="Appointments")


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
                record.age = date.today().year - record.date_of_birth.year
            else:
                record.age = 0
    ## end dependant functions ##

    ## get functions ##
    def name_get(self):
        res = []
        for rec in self:
            name = "[" + str(rec.id) + "] " + rec.name
            res.append((rec.id, name))
        return res
    ## end get functions ##

    ## overrides ##
    def unlink(self):
        for rec in self:
            if rec.state == 'done':
                raise ValidationError(f"you cannot delete use {rec.name} as it is in Done state")
            for appointment in rec.appointment_ids:
                appointment.unlink()
            super(HospitalPatient, rec).unlink()

    def copy(self, default={}):
        if not default.get('name'):
            default['name'] = f"{self.name} (COPY)"
        return super(HospitalPatient, self).copy(default)
    ## end overrides ##

    ## constrains ##

    @api.constrains('name')
    def check_name(self):
        patient = self.env['hospital.patient']
        for rec in self:
            search = patient.search([('name', '=', rec.name), ('id', '!=', rec.id)])
            if search:
                raise ValidationError(f'the name {rec.name} already exists')

    @api.constrains('age')
    def check_age(self):
        for rec in self:
            if rec.age == 0:
                raise ValidationError('the age cannot be 0')
    ## end constrains ##

    ## end functions ##
