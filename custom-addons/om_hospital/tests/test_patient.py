from odoo.tests import common
import datetime
class TestModelA(common.TransactionCase):
    def test_some_action(self):
        record = self.env['hospital.patient'].create({'name': 'fg002', 'ref': 1, 'date_of_birth': datetime.datetime(2000,12,12)})

        print('\n\n\n\n\n\n\n\n', record, '\n\n\n\n\n\n\n\n')

        self.assertEqual(
            record.age,
            datetime.date.today().year-datetime.datetime(2000, 12, 12).year)

        record.action_confirm()
        self.assertEqual(
            record.state,
            'confirm')