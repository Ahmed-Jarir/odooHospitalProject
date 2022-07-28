from odoo.tests import common
from odoo.exceptions import ValidationError
import datetime
class TestModelB(common.TransactionCase):
    def test_some_action(self):
        doc = self.env['hospital.doctors'].create({'name': 'doc003', 'date_of_birth': datetime.datetime(1950, 12, 12)})
        record2 = self.env['hospital.patient'].create({'name': 'fg003', 'ref': doc.id, 'date_of_birth': datetime.datetime(2000, 12, 12)})

        with self.assertRaises(ValidationError):
            self.env['create.appointment.wizard'].create({'patient_id': record2.id, 'doctor': doc.id, 'appointment_time': datetime.datetime(2020, 12, 12)})


        self.env['create.appointment.wizard'].create({'patient_id': record2.id, 'doctor': doc.id, 'appointment_time': datetime.datetime(datetime.datetime.today().year+1, 12, 12)})
