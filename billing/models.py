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