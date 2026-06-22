"""

from django.test import TestCase

# Create your tests here.
"""
# this is the new added
from django.test import TestCase
from django.core.exceptions import ValidationError
from datetime import timedelta
from django.utils import timezone
from .models import Patient

class PatientModelTest(TestCase):

    def test_cannot_register_future_birthdays(self):
        """ Grade 6 safety check: Attempting to register a birthday in tomorrow's timeline must FAIL. """
        tomorrow = timezone.now().date() + timedelta(days=1)
        
        patient = Patient(
            first_name="Kidus",
            last_name="Tadesse",
            gender="M",
            date_of_birth=tomorrow,
            phone_number="+251911223344"
        )
        
        with self.assertRaises(ValidationError):
            patient.save()

    def test_name_string_auto_cleaning(self):
        """ Tests that spaces are trimmed out and titles get formatted perfectly. """
        patient = Patient.objects.create(
            first_name="  marta  ",
            last_name="asfaw",
            gender="F",
            phone_number="0912345678"
        )
        self.assertEqual(patient.first_name, "Marta")
        self.assertEqual(patient.last_name, "Asfaw")