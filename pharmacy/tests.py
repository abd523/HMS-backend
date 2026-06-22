from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone
from datetime import timedelta
from .models import Medicine

class MedicineModelTest(TestCase):

    def test_cannot_save_negative_or_corrupt_stock_values(self):
        """ Grade 6 safety check: Passing a sub-zero medicine count must fail instantly. """
        tomorrow = timezone.now().date() + timedelta(days=100)
        med = Medicine(
            name="Amoxicillin 500mg",
            category="Antibiotic",
            quantity_in_stock=-5, # Bad data
            price_per_unit=15.50,
            expiry_date=tomorrow
        )
        with self.assertRaises(ValidationError):
            med.save()

    def test_medicine_expiry_property_logic(self):
        """ Checks if our expiration flagging logic successfully isolates outdated drugs. """
        yesterday = timezone.now().date() - timedelta(days=1)
        expired_med = Medicine.objects.create(
            name="Paracetamol 500mg",
            category="Painkiller",
            quantity_in_stock=100,
            price_per_unit=2.00,
            expiry_date=yesterday
        )
        self.assertTrue(expired_med.is_expired)



"""
from django.test import TestCase

# Create your tests here.
"""