from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings
# THE NEW ADDED FEATURE
from django.core.validators import RegexValidator

class User(AbstractUser):
    class Role(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        DOCTOR = 'DOCTOR', 'Doctor'
        NURSE = 'NURSE', 'Nurse'
        RECEPTIONIST = 'RECEPTIONIST', 'Receptionist'
        PHARMACIST = 'PHARMACIST', 'Pharmacist'
        LAB_TECHNICIAN = 'LAB_TECHNICIAN', 'Lab Technician'
        PATIENT = 'PATIENT', 'Patient'

    role = models.CharField(max_length=20, choices=Role.choices, default=Role.PATIENT)
    
    # Grade 6 rule: Make sure phone numbers are only numbers!
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number must be valid.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15, blank=True, null=True)
    
    is_approved = models.BooleanField(default=False)  # ለሰራተኞች ፍቃድ መስጫ
# THE NEW ADDED FEATURE
    def save(self, *args, **kwargs):
        # Grade 6 rule: If they are a patient, they don't need staff approval to use the app
        if self.role == self.Role.PATIENT:
            self.is_approved = True
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.username} - {self.role}"


class AuditLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)
    timestamp = models.DateTimeField(auto_now_add=True)
# THE NEW ADDED FEATURE
    class Meta:
        ordering = ['-timestamp'] # Newest logs show up first!

    def __str__(self):
        return f"{self.user} performed {self.action} at {self.timestamp}"