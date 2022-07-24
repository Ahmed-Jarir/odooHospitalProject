from datetime import date
from odoo import api, fields, models
from odoo.odoo import exceptions


class HospitalDoctors(models.Model):
    _name = "hospital.doctors"
    _inherit=["mail.thread", "mail.activity.mixin"]
    _description = "hospital_doctors"

    image = fields.Binary(string="Doctors image")
    name = fields.Char(string='Name', required=True, translate=True, Tracking=True)

    date_of_birth = fields.Date(string='Date of birth', Tracking=True)
    age = fields.Integer(string='Age', compute='_compute_age', Tracking=True)
    gender = fields.Selection([('male','Male'), ('female','Female')],string= 'Gender', Tracking=True)

    @api.depends('date_of_birth')
    def _compute_age(self):
        for record in self:
            if record.date_of_birth and record.date_of_birth.year < date.today().year:
                #tempAge = date.today().year - record.date_of_birth.year
                record.age = date.today().year - record.date_of_birth.year
            else:
                record.age = 0