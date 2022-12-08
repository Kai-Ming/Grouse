"""Unit tests for the record transfer form"""
from django.test import TestCase
from lessons.models import Transfer
from lessons.forms import RecordTransferForm
import datetime

class RecordTransferFormTestCase(TestCase):

    def test_amount_cant_be_empty(self):
        input = {'amount':10, 'invoice_number': 100-00, 'date': datetime.date.today()}
        form = RecordTransferForm(data=input)
        self.assertTrue(form.is_valid())

    def test_invoice_number_cant_be_empty(self):
        input = {'amount':10, 'date': datetime.date.today()}
        form = RecordTransferForm(data=input)
        self.assertFalse(form.is_valid())

    def test_date_cant_be_empty(self):
        input = {'amount':10, 'invoice_number': 100-00}
        form = RecordTransferForm(data=input)
        self.assertFalse(form.is_valid())

