from rest_framework import serializers
from .models import LabRequest, LabTest

class LabRequestSerializer(serializers.ModelSerializer):
    patient_name = serializers.ReadOnlyField(source='patient.first_name')
    doctor_name = serializers.ReadOnlyField(source='doctor.__str__')

    class Meta:
        model = LabRequest
        fields = '__all__'

class LabTestSerializer(serializers.ModelSerializer):
    patient_name = serializers.ReadOnlyField(source='patient.first_name')
    
    class Meta:
        model = LabTest
        fields = '__all__'
        read_only_fields = ['completed_at'] # Controlled by the system



"""
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

        """