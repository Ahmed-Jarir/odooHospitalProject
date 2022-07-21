from odoo import api, fields, models


class HospitalAppointment(models.Model):
    _name = "hospital.appointment"
    _inherit=["mail.thread", "mail.activity.mixin"]
    _description = "hospital_appointment"

    patient_id = fields.Many2one('hospital.patient', string='Patient')

    gender = fields.Selection(related='patient_id.gender')
    appointment_time = fields.Datetime(string='Appointment Time', default=fields.Datetime.now)
    booking_date = fields.Date(string="Booking Date", default=fields.Date.context_today)

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

    ## end functions ##
