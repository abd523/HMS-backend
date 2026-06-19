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