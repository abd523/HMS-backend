from django.db import models
from django.core.exceptions import ValidationError
from patients.models import Patient
from doctors.models import Doctor

class MedicalRecord(models.Model):
    # Grade 6 rule: PROTECT blocks anyone from erasing clinical medical history!
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='medical_records')
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT)
    
    diagnosis = models.TextField()
    doctor_notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Grade 6 rule: A medical chart must include an actual diagnosis.
        if self.diagnosis and not self.diagnosis.strip():
            raise ValidationError("Diagnosis cannot be empty text space.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Record #{self.id} for {self.patient} - {self.created_at.date()}"


class Prescription(models.Model):
    # If a medical record is wiped, its single prescription sheet can drop safely with CASCADE
    record = models.OneToOneField(MedicalRecord, on_delete=models.CASCADE, related_name='prescription')
    
    # Expected format: [{"medicine_id": 1, "name": "Amoxicillin", "dosage": "500mg", "frequency": "3x daily"}]
    medications = models.JSONField() 
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Grade 6 rule: Don't allow writing a completely empty drug slip prescription.
        if not self.medications:
            raise ValidationError("Prescription must contain at least one medication entry.")

    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Prescription #{self.id} for Record #{self.record.id}"


"""
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

    """