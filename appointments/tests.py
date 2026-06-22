"""from django.test import TestCase

# Create your tests here."""
from django.test import TestCase
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from datetime import timedelta

# Import your models (Make sure your patient/doctor app structures match)
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment

User = get_user_model()

class AppointmentModelTest(TestCase):

    def setUp(self):
        """
        Grade 6 definition: Setting up the toys before we play!
        This creates a fake patient and a fake doctor in a temporary 
        test database so we can try making appointments with them.
        """
        # 1. Create a fake user for the doctor
        self.doc_user = User.objects.create_user(
            username="dr_yohannes", 
            password="securepassword123",
            role="DOCTOR"
        )
        # 2. Link them to the Doctor model
        self.doctor = Doctor.objects.create(user=self.doc_user, specialization="General Physician")
        
        # 3. Create a fake Patient
        self.patient = Patient.objects.create(first_name="Abel", last_name="Kebede", age=25)

    def test_create_successful_appointment(self):
        """ Tests if a normal, correct appointment saves perfectly. """
        appointment = Appointment.objects.create(
            patient=self.patient,
            doctor=self.doctor,
            appointment_date=timezone.now().date(),
            appointment_time="10:00:00",
            reason="Regular checkup"
        )
        # Check if it actually saved in our test database
        self.assertEqual(Appointment.objects.count(), 1)
        self.assertEqual(appointment.status, 'Pending')

    def test_cannot_book_appointment_in_the_past(self):
        """
        Grade 6 test: Making sure our time machine blocker works!
        If someone tries to book an appointment for yesterday, it should FAIL.
        """
        yesterday = timezone.now().date() - timedelta(days=1)
        
        # We expect a ValidationError to happen here
        with self.assertRaises(ValidationError):
            appointment = Appointment(
                patient=self.patient,
                doctor=self.doctor,
                appointment_date=yesterday,
                appointment_time="14:00:00",
                reason="This should fail!"
            )
            appointment.save() # This triggers the validation clean() method