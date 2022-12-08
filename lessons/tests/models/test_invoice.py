from django.test import TestCase
from django.core.exceptions import ValidationError
from lessons.models import Invoice
import datetime


class InvoiceModelTestCase(TestCase):
    """Unit tests for the Invoice model."""


    # Sets up an example invoice to be used for tests
    def setUp(self):
        self.invoice = Invoice.objects.create(
            invoice_no='1234-1234',
            due_amount='12.34',
            due_date=datetime.datetime.now(),
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )


    # Tests if the invoice is valid
    def test_valid_invoice(self):
        self._assert_invoice_is_valid()


    # Tests the fact that invoice_no field should not be blank
    def test_invoice_number_must_not_be_blank(self):
        self.invoice.invoice_no = ''
        self._assert_invoice_is_invalid()


    # Tests the fact that invoice_no field should not be too long
    def test_invoice_number_too_long(self):
        self.invoice.invoice_no = '12345678901234567890123456789-12345678901234567890123456789'
        self._assert_invoice_is_invalid() 


    # Tests the fact that due_amount field should not be blank
    def test_due_amount_must_not_be_blank(self):
        self.invoice.due_amount = ''
        self._assert_invoice_is_invalid()


    # Tests the fact that due_amount field should be an int
    def test_due_amount_is_int(self):
        if self.invoice.due_amount != int(float(self.invoice.due_amount)):
            self._assert_invoice_is_invalid


    # Tests the fact that due_amount field should not have more than two decimal places in it
    def test_due_amount_must_not_have_more_than_two_decimal_places(self):
        self.invoice.due_amount = '1.234'
        self._assert_invoice_is_invalid()


    """Helper functions"""


    # Asserts that invoice is valid
    def _assert_invoice_is_valid(self):
        try:
            self.invoice.full_clean()
        except ValidationError:
            self.fail('Test invoice is not valid.')


    # Asserts that invoice is invalid
    def _assert_invoice_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.invoice.full_clean()
