from datetime import date
from odoo import api, fields, models
from odoo.odoo import exceptions


class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit=["mail.thread", "mail.activity.mixin"]
    _description = "hospital_patient"

    name = fields.Char(string='Name', required=True, translate=True, Tracking=True)
    ref = fields.Char(string='Reference', Tracking=True)
    date_of_birth = fields.Date(string='Date of birth')
    age = fields.Integer(string='Age', compute='_compute_age', Tracking=True)
    gender = fields.Selection([('male','Male'), ('female','Female')],string= 'Gender', Tracking=True)
    active = fields.Boolean(string='active', default=True)


    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth and record.date_of_birth.year < date.today().year:
                #tempAge = date.today().year - record.date_of_birth.year
                record.age = date.today().year - record.date_of_birth.year
            else:
                record.age = 0