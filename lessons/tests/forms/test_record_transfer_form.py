"""Unit tests for the record transfer form"""
from django.test import TestCase
from lessons.models import Transfer
from lessons.forms import RecordTransferForm
import datetime

class RecordTransferFormTestCase(TestCase):
    """Tester Class for Record Transfer Form"""


    # Test the form is invalid if the amount field is empty
    def test_amount_cant_be_empty(self):
        input = {'invoice_number': 100-00, 'date': datetime.date.today()}
        form = RecordTransferForm(data=input)
        self.assertFalse(form.is_valid())


    # Test the form is invalid if the number field is empty
    def test_invoice_number_cant_be_empty(self):
        input = {'amount':10, 'date': datetime.date.today()}
        form = RecordTransferForm(data=input)
        self.assertFalse(form.is_valid())


    # Test the form is invalid if the date field is empty
    def test_date_cant_be_empty(self):
        input = {'amount':10, 'invoice_number': 100-00}
        form = RecordTransferForm(data=input)
        self.assertFalse(form.is_valid())

