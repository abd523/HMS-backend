from django.db import models
from django.core.exceptions import ValidationError
from django.utils import timezone
from patients.models import Patient
from doctors.models import Doctor

class LabRequest(models.Model):
    STATUS_CHOICES = [('Pending', 'Pending'), ('Completed', 'Completed')]

    # Grade 6 rule: PROTECT stops medical history from being erased by accident!
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='lab_requests')
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT, related_name='lab_requests')
    test_name = models.CharField(max_length=150) # e.g., CBC, Widal Test
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request: {self.test_name} for {self.patient}"


class LabTest(models.Model):
    TEST_STATUS = [('Pending', 'Pending'), ('Completed', 'Completed')]

    # Grade 6 rule: Link the test directly back to the original doctor request
    lab_request = models.OneToOneField(LabRequest, on_delete=models.SET_NULL, null=True, blank=True, related_name='test_result_record')
    patient = models.ForeignKey(Patient, on_delete=models.PROTECT, related_name='lab_tests')
    doctor = models.ForeignKey(Doctor, on_delete=models.PROTECT) # Ordering Doctor
    
    test_name = models.CharField(max_length=100)
    test_result = models.TextField(blank=True, null=True) # The actual findings
    status = models.CharField(max_length=20, choices=TEST_STATUS, default='Pending')
    ordered_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def clean(self):
        # Grade 6 rule: You cannot say a test is "Completed" if you left the result empty!
        if self.status == 'Completed' and not self.test_result:
            raise ValidationError("You must provide test results before marking this test as completed.")

    def save(self, *args, **kwargs):
        self.full_clean()
        
        # Grade 6 rule: Automatically stamp the time when finished, and update the doctor's request status too!
        if self.status == 'Completed' and not self.completed_at:
            self.completed_at = timezone.now()
            if self.lab_request:
                self.lab_request.status = 'Completed'
                self.lab_request.save()
        elif self.status == 'Pending':
            self.completed_at = None
            
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.test_name} Result for {self.patient}"





"""
from django.db import models
from patients.models import Patient
from doctors.models import Doctor

# 1. አዲሱ የላብ ማዘዣ/ጥያቄ ሞዴል (LabRequest)
class LabRequest(models.Model):
    STATUS_CHOICES = [('Pending', 'Pending'), ('Completed', 'Completed')]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    test_name = models.CharField(max_length=150) # e.g., CBC, Widal Test
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
    result_details = models.TextField(blank=True, null=True) # የምርመራ ውጤት ማጠቃለያ
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Request: {self.test_name} for {self.patient}"


# 2. የነበረው የላብ ምርመራ ሞዴል (LabTest)
class LabTest(models.Model):
    TEST_STATUS = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
    ]

    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, related_name='lab_tests')
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE) # ያዘዘው ሐኪም
    test_name = models.CharField(max_length=100) # የምርመራ ዓይነት (e.g., CBC, X-Ray)
    test_result = models.TextField(blank=True, null=True) # የምርመራ ውጤት
    status = models.CharField(max_length=20, choices=TEST_STATUS, default='Pending')
    ordered_at = models.DateTimeField(auto_now_add=True)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"{self.test_name} for {self.patient}"

        """