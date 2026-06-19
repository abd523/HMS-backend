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