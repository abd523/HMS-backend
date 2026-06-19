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