"""

from django.test import TestCase

# Create your tests here.
"""

# this is the new added feaure

from django.test import TestCase
from django.core.exceptions import ValidationError
from patients.models import Patient
from doctors.models import Doctor
from django.contrib.auth import get_user_model
from .models import LabTest

User = get_user_model()

class LabTestModelTest(TestCase):

    def setUp(self):
        self.patient = Patient.objects.create(first_name="Yonas", last_name="Alemu", gender="M")
        self.user = User.objects.create_user(username="dr_kassa", role="DOCTOR")
        self.doctor = Doctor.objects.create(user=self.user, specialization="Pathology")

    def test_cannot_complete_test_without_results(self):
        """ Grade 6 safety check: Block technicians from saving a finished test with empty text notes. """
        test = LabTest(
            patient=self.patient,
            doctor=self.doctor,
            test_name="Blood Sugar Test",
            status="Completed",
            test_result="" # Empty!
        )
        
        with self.assertRaises(ValidationError):
            test.save()