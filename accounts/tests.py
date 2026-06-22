"""from django.test import TestCase

# Create your tests here.
"""

# this is the new added festure it was empty before

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError

User = get_user_model()

class UserModelTest(TestCase):

    def test_create_normal_patient_auto_approves(self):
        """
        Grade 6 test: Making sure patients can log in immediately!
        When a user registers as a PATIENT, they should be automatically approved.
        """
        patient_user = User.objects.create_user(
            username="patient_kidus",
            email="kidus@example.com",
            password="patientpassword123",
            role="PATIENT"
        )
        
        # Check if the role is correct
        self.assertEqual(patient_user.role, "PATIENT")
        # Check if our custom save() rule made them True automatically
        self.assertTrue(patient_user.is_approved)

    def test_create_doctor_requires_admin_approval(self):
        """
        Grade 6 test: Making sure staff members wait for approval!
        When a DOCTOR registers, they should stay unapproved (False) 
        until an Admin manually activates them.
        """
        doctor_user = User.objects.create_user(
            username="dr_selam",
            email="selam@example.com",
            password="doctorpassword123",
            role="DOCTOR"
        )
        
        self.assertEqual(doctor_user.role, "DOCTOR")
        # Doctors should NOT be auto-approved! It must be False.
        self.assertFalse(doctor_user.is_approved)

    def test_password_is_safely_hashed(self):
        """
        Grade 6 test: Checking the secret password lock.
        The database should never save plain text passwords. It must encrypt them.
        """
        secret_password = "my_super_secret_123"
        user = User.objects.create_user(
            username="test_security",
            password=secret_password,
            role="PATIENT"
        )
        
        # Verify Django's check_password tool can read it, but the database string is mixed up
        self.assertTrue(user.check_password(secret_password))
        self.assertNotEqual(user.password, secret_password)