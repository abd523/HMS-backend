from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone

class Medicine(models.Model):
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50) # e.g., Antibiotic, Painkiller
    
    # Grade 6 rule: Stock numbers cannot drop below 0!
    quantity_in_stock = models.IntegerField(default=0)
    
    # Grade 6 rule: Medicine costs cannot be negative or free!
    price_per_unit = models.DecimalField(max_digits=8, decimal_places=2)
    expiry_date = models.DateField() # Removed the default today parameter to force explicit data inputs

    def clean(self):
        if self.quantity_in_stock is not None and self.quantity_in_stock < 0:
            raise ValidationError("Quantity in stock cannot drop below zero.")
        if self.price_per_unit is not None and self.price_per_unit <= 0:
            raise ValidationError("Price per unit must be a positive number greater than zero.")

    def save(self, *args, **kwargs):
        self.full_clean() # Triggers our math validations automatically before write states
        super().save(*args, **kwargs)

    @property
    def is_expired(self):
        # Grade 6 rule: Easy calculated calculation flag to pinpoint bad medication batches instantly
        return self.expiry_date < timezone.now().date()

    def __str__(self):
        return f"{self.name} ({self.quantity_in_stock} left)"


"""
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

        """