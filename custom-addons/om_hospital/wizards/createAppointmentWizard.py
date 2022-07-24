from odoo import api, fields, models


class CreateAppointmentWizard(models.TransientModel):
    _name = "create.appointment.wizard"
    _inherit=["mail.thread", "mail.activity.mixin"]
    _description = "hospital_appointment"

    appointment_time = fields.Datetime(string='time', required=True)
    patient_id = fields.Many2one('hospital.patient', string='Patient', required=True)
    doctor = fields.Many2one("hospital.doctors", string="doctor", required=True)

    def make_an_appointment(self):
        vals = {
            "patient_id": self.patient_id.id,
            "appointment_time": self.appointment_time,
            "doctor": self.doctor.id
        }
        self.env['hospital.appointment'].create(vals)
    def view_appointments(self):
        action = self.env.ref('om_hospital.action_hospital_appointment').read()[0]
        action['domain'] = [('patient_id', '=', self.patient_id.id)]
        return action