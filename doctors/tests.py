"""

from django.test import TestCase

# Create your tests here.
"""
# this was empty 
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from .models import Doctor

User = get_user_model()

class DoctorModelTest(TestCase):

    def setUp(self):
        # Create a user model record container to attach our doctor profile onto
        self.user = User.objects.create_user(
            username="dr_abebe",
            password="password123",
            role="DOCTOR",
            first_name="Abebe",
            last_name="Chala"
        )

    def test_create_doctor_profile_successfully(self):
        """ Tests if valid doctor fields save without issues. """
        doctor = Doctor.objects.create(
            user=self.user,
            specialization="Cardiology",
            license_number="DM-12345",
            experience_years=8
        )
        self.assertEqual(Doctor.objects.count(), 1)
        self.assertTrue(doctor.is_available)

    def test_cannot_save_negative_experience_values(self):
        """ Grade 6 safety check: Block impossible negative work history data counts. """
        with self.assertRaises(ValidationError):
            bad_doctor = Doctor(
                user=self.user,
                specialization="Pediatrics",
                license_number="DM-54321",
                experience_years=-3
            )
            bad_doctor.save()