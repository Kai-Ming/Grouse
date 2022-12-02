from django.test import TestCase
from django.core.exceptions import ValidationError
from lessons.models import Invoice
import datetime


class InvoiceModelTestCase(TestCase):
    """Unit tests for the Invoice model."""

    def setUp(self):
        self.invoice = Invoice.objects.create(
            invoice_no='1234-1234',
            due_amount='12.34',
            due_date=datetime.datetime.now(),
            created_at=datetime.datetime.now(),
            updated_at=datetime.datetime.now()
        )

    def test_valid_invoice(self):
        self._assert_invoice_is_valid()

    # Invoice number
    def test_invoice_number_must_not_be_blank(self):
        self.invoice.invoice_no = ''
        self._assert_invoice_is_invalid()

    # Due amount
    def test_due_amount_must_not_be_blank(self):
        self.invoice.due_amount = ''
        self._assert_invoice_is_invalid()

    def test_due_amount_must_not_have_more_than_two_decimal_places(self):
        self.invoice.due_amount = '1.234'
        self._assert_invoice_is_invalid()

    # Helper functions
    def _assert_invoice_is_valid(self):
        try:
            self.invoice.full_clean()
        except ValidationError:
            self.fail('Test invoice is not valid.')

    def _assert_invoice_is_invalid(self):
        with self.assertRaises(ValidationError):
            self.invoice.full_clean()
