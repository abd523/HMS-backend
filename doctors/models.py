from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Doctor(models.Model):
    # Grade 6 rule: PROTECT keeps database records safe even if someone deletes a user account login by mistake!
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name='doctor_profile')
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    experience_years = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def clean(self):
        # Grade 6 rule: A doctor cannot have negative experience years!
        if self.experience_years < 0:
            raise ValidationError("Experience years cannot be a negative number.")

    def save(self, *args, **kwargs):
        self.full_clean() # Triggers our rules automatically
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name} ({self.specialization})"




"""
from django.db import models
from django.conf import settings

class Doctor(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='doctor_profile')
    specialization = models.CharField(max_length=100)
    license_number = models.CharField(max_length=50, unique=True)
    # እዚህ ጋር default=0 ተደርጓል
    experience_years = models.IntegerField(default=0)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"Dr. {self.user.first_name} {self.user.last_name} ({self.specialization})"


        """