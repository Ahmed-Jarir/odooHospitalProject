from odoo.tests import common
from odoo.exceptions import ValidationError
import datetime
class TestModelA(common.TransactionCase):
    def test_some_action(self):
        record = self.env['hospital.patient'].create({'name': 'fg001', 'ref': 1, 'date_of_birth': datetime.datetime(2000,12,12)})

        print('\n\n\n\n\n\n\n\n', record, '\n\n\n\n\n\n\n\n')

        self.assertEqual(
            record.age,
            datetime.date.today().year-datetime.datetime(2000, 12, 12).year)

        record.action_confirm()
        self.assertEqual(
            record.state,
            'confirm')
        record.action_done()
        self.assertEqual(
            record.state,
            'done')
        newRec = record.copy()
        self.assertEqual(
            newRec.name,
            f"{record.name} (COPY)")
        ## check if name constraint is not working
        with self.assertRaises(ValidationError):
            self.env['hospital.patient'].create({'name': 'fg002', 'ref': 1, 'date_of_birth': datetime.datetime(2000,12,12)})
        ## check if age constraint is not working
        with self.assertRaises(ValidationError):
            record.setDOB(datetime.datetime.today())
        ## check for unlink error
        with self.assertRaises(ValidationError):
            record.unlink()


        record.action_cancel()
        newRec.unlink()
        record.unlink()
