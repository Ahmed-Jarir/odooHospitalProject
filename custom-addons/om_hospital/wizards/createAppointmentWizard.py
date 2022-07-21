from odoo import api, fields, models


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _inherit=["mail.thread", "mail.activity.mixin"]
    _description = "hospital_appointment"

    name = fields.Char(string='Name', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient')

    def make_an_appointment(self):
        print("")