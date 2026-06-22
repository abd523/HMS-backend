from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
from django.utils import timezone

class Patient(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    
    # Grade 6 rule: Block letter typos from making their way into phone numbers!
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="Phone number format is invalid.")
    phone_number = models.CharField(validators=[phone_regex], max_length=15)
    
    email = models.EmailField(blank=True, null=True)
    address = models.TextField(blank=True, default="")
    medical_history = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def clean(self):
        # Grade 6 rule: You can't be born tomorrow! 
        if self.date_of_birth and self.date_of_birth > timezone.now().date():
            raise ValidationError("Date of birth cannot be a future date.")

    def save(self, *args, **kwargs):
        # Grade 6 tip: Clean up whitespace and capitalize names cleanly (e.g., "  abel " -> "Abel")
        if self.first_name:
            self.first_name = self.first_name.strip().capitalize()
        if self.last_name:
            self.last_name = self.last_name.strip().capitalize()
            
        self.full_clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"




"""

from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = [('M', 'Male'), ('F', 'Female')]

    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(blank=True, null=True)
    
    # እዚህ ጋር default="" እና blank=True በማድረጋችን የቆዩት ታካሚዎች ላይ በራሱ ባዶ ጽሑፍ ይሞላል
    address = models.TextField(blank=True, default="")
    
    medical_history = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

        """