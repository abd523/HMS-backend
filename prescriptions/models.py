from django.db import models
from patients.models import Patient
from doctors.models import Doctor

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='medical_records')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    doctor_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

class Prescription(models.Model):
    record = models.OneToOneField(MedicalRecord, on_delete=models.CASCADE, related_name='prescription')
    medications = models.JSONField() # የአወሳሰድ መመሪያን በJSON ፎርማት ለመያዝ
    created_at = models.DateTimeField(auto_now_add=True)