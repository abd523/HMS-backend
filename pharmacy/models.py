from django.db import models
from django.utils import timezone # 1. የጊዜ ዞኑን እዚህ አስገብተናል

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50) # e.g., Antibiotic, Painkiller
    quantity_in_stock = models.IntegerField(default=0)
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)
    
    # 2. default=timezone.now በማድረግ ለቆዩትም ሆነ ለአዲሶቹ ነባሪ እሴት ሰጥተናል
    expiry_date = models.DateField(default=timezone.now)

    def __str__(self):
        return f"{self.name} ({self.quantity_in_stock} left)"