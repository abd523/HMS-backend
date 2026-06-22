from django.db import models
from django.core.exceptions import ValidationError
from patients.models import Patient
from django.utils import timezone

class Invoice(models.Model):
    STATUS_CHOICES = [('Unpaid', 'Unpaid'), ('Paid', 'Paid')]

    # Grade 6 rule: Changing to PROTECT stops anyone from accidentally erasing critical money records!
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='invoices')
    
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Unpaid')
    created_at = models.DateTimeField(auto_now_add=True)
    paid_at = models.DateTimeField(blank=True, null=True)

    def clean(self):
        # Grade 6 rule: Bills cannot be zero or negative numbers!
        if self.total_amount is not None and self.total_amount <= 0:
            raise ValidationError("Invoice amount must be a positive number greater than zero.")

    def save(self, *args, **kwargs):
        # Automatically stamp the time whenever status becomes Paid
        if self.status == 'Paid' and not self.paid_at:
            self.paid_at = timezone.now()
        elif self.status == 'Unpaid':
            self.paid_at = None # Clears if marked back down
            
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Invoice #{self.id} - {self.patient} ({self.status})"






"""
from django.db import models
# ከታካሚው አፕ ላይ የPatient ሞዴልን እዚህ ጋር አስገብተናል
from patients.models import Patient
from django.utils import timezone


class Invoice(models.Model):
    # የክፍያ ሁኔታዎችን መለያ ዝርዝር (Choices)
    STATUS_CHOICES = [('Unpaid', 'Unpaid'), ('Paid', 'Paid')]

    # ከታካሚው ጋር ማገናኛ (ForeignKey)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    
    # ጠቅላላ የክፍያ መጠን (የድሮው 'amount' ወደ 'total_amount' ተቀይሯል)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    
    # የክፍያ ሁኔታ (በነባሪ Unpaid ይሆናል)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Unpaid')
    
    # ኢንቮይሱ የተፈጠረበት እና የተከፈለበት ጊዜ
    created_at = models.DateTimeField(auto_now_add=True)
    
    # ክፍያው ሲፈጸም ብቻ የሚሞላ (ስለዚህ null=True መሆን አለበት)
    paid_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Invoice #{self.id} - {self.patient} ({self.status})"


        """