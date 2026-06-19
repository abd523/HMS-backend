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