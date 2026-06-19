from django.contrib.auth.models import AbstractUser
from django.db import models
from django.conf import settings


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
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    is_approved = models.BooleanField(default=False)  # ለሰራተኞች ፍቃድ መስጫ

    def __str__(self):
        return f"{self.username} - {self.role}"


class AuditLog(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=255)  # e.g., "Collected Payment for Invoice #12"
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} performed {self.action} at {self.timestamp}"