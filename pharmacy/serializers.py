from rest_framework import serializers
from .models import Medicine

class MedicineSerializer(serializers.ModelSerializer):
    # Sends a clean True/False flag straight to Next.js so you can color code expired drugs in red
    is_expired = serializers.ReadOnlyField()

    class Meta:
        model = Medicine
        fields = ['id', 'name', 'category', 'quantity_in_stock', 'price_per_unit', 'expiry_date', 'is_expired']
"""
from rest_framework import serializers
from .models import Medicine

class MedicineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicine
        fields = '__all__'
        """