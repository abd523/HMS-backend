from rest_framework import serializers
from .models import LabRequest, LabTest

class LabRequestSerializer(serializers.ModelSerializer):
    patient_name = serializers.ReadOnlyField(source='patient.first_name')
    class Meta:
        model = LabRequest
        fields = '__all__'

class LabTestSerializer(serializers.ModelSerializer):
    patient_name = serializers.ReadOnlyField(source='patient.first_name')
    class Meta:
        model = LabTest
        fields = '__all__'