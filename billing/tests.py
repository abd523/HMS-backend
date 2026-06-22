"""
from django.test import TestCase

# Create your tests here.
"""
# thsi feature was not created

from django.test import TestCase
from django.core.exceptions import ValidationError
from patients.models import Patient
from .models import Invoice

class InvoiceModelTest(TestCase):

    def setUp(self):
        # Mock up sample environment data parameters
        self.patient = Patient.objects.create(first_name="Natnael", last_name="Asefa", gender="M")

    def test_invoice_auto_timestamps_on_payment(self):
        """ Tests that paying a bill triggers our automatic system clock tracking stamp. """
        invoice = Invoice.objects.create(patient=self.patient, total_amount=250.00, status='Unpaid')
        self.assertNil = self.assertIsNone(invoice.paid_at)

        # Shift status parameters up to Paid
        invoice.status = 'Paid'
        invoice.save()

        self.assertIsNotNone(invoice.paid_at)

    def test_cannot_create_negative_invoice_amounts(self):
        """ Grade 6 safety check: Ensuring negative price limits throw errors automatically. """
        with self.assertRaises(ValidationError):
            bad_invoice = Invoice(patient=self.patient, total_amount=-100.00, status='Unpaid')
            bad_invoice.save()