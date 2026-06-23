# appointments/models.py
import uuid
from django.db import models
from django.db.models import Q, CheckConstraint, UniqueConstraint
from core.models import TrackingModel 

class Appointment(TrackingModel): 
    STATUS_CHOICES = [
        ('Scheduled', 'Scheduled'),
        ('Completed', 'Completed'),
        ('Cancelled', 'Cancelled'),
    ]

    # Allows null=True and blank=True so old data doesn't conflict during the UUID transition
    doctor = models.ForeignKey(
        'doctors.Doctor', 
        on_delete=models.CASCADE, 
        related_name='appointments',
        null=True,
        blank=True
    )
    patient = models.ForeignKey(
        'patients.Patient', 
        on_delete=models.CASCADE, 
        related_name='appointments',
        null=True,
        blank=True
    )
    
    appointment_date = models.DateField(db_index=True) 
    appointment_time = models.TimeField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Scheduled')
    
    # ✅ Fixed: Added blank=True and default="" to satisfy fallback data validation rules
    reason = models.TextField(blank=True, default="")

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['doctor', 'appointment_date', 'appointment_time'],
                name='unique_doctor_schedule_slot',
                condition=Q(deleted_at__isnull=True) 
            ),
            CheckConstraint(
                check=Q(status__in=['Scheduled', 'Completed', 'Cancelled']),
                name='valid_appointment_status'
            )
        ]

    def __str__(self):
        return f"Appt {self.id} - Dr. {self.doctor} with Patient {self.patient}"

"""
from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from patients.models import Patient
from doctors.models import Doctor

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    ]

    # Grade 6 rule: If a patient profile is deleted, do NOT delete the appointment history record!
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True, related_name='appointments')
    
    # Safely calls the current system date
    appointment_date = models.DateField(default=timezone.now)
    
    # Grade 6 rule fixed: Uses a small function to correctly grab only the current time
    appointment_time = models.TimeField(default=timezone.localtime)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    reason = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Grade 6 rule: You can't travel back in time! Appointments must be for today or the future.
        if self.appointment_date < timezone.now().date():
            raise ValidationError("You cannot schedule an appointment for a past date.")

    def save(self, *args, **kwargs):
        self.full_clean() # Runs the clean validation rule written above automatically
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.patient} with {self.doctor} on {self.appointment_date}"


"""

"""
from django.db import models
from django.utils import timezone
from patients.models import Patient
from doctors.models import Doctor

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='appointments')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE, related_name='appointments')
    
    # በነባሪ የአሁኑን ቀን ለመያዝ timezone.now.date (ያለ ቅንፍ)
    appointment_date = models.DateField(default=timezone.now)
    
    # በነባሪ የአሁኑን ሰዓት ለመያዝ በላምብዳ ፈንክሽን timezone.now().time() ማድረጉ ይመረጣል
    appointment_time = models.TimeField(default=timezone.now)
    
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    reason = models.TextField(blank=True, null=True)
    
    # ተርሚናሉ ላይ 1 ብለህ ካሳለፍክ በኋላ ይህ መስመር በትክክል ይሠራል
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.patient} with {self.doctor} on {self.appointment_date}"


        """