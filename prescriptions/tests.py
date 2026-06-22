"""
from django.test import TestCase

# Create your tests here.
"""

# this is the new added feature

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from django.db.models import PROTECT
from patients.models import Patient
from doctors.models import Doctor
from .models import MedicalRecord

User = get_user_model()

class MedicalRecordModelTest(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(first_name="Helena", last_name="Bekele", gender="F")
        self.user = User.objects.create_user(username="dr_alemu", role="DOCTOR")
        self.doctor = Doctor.objects.create(user=self.user, specialization="Internal Medicine")

    def test_cannot_save_blank_diagnosis(self):
        """ Grade 6 safety check: Ensuring empty charts are strictly rejected. """
        record = MedicalRecord(
            patient=self.patient,
            doctor=self.doctor,
            diagnosis="   " # Blank text spaces
        )
        with self.assertRaises(ValidationError):
            record.save()

    def test_patient_deletion_is_protected(self):
        """ Grade 6 safety check: Deleting a patient profile must be blocked if active charts exist. """
        MedicalRecord.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            diagnosis="Acute Gastritis"
        )
        
        # Trying to delete the patient should trigger a ProtectedError exception
        with self.assertRaises(models.ProtectedError if hasattr(models, 'ProtectedError') else Exception):
            self.patient.delete()