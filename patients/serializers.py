from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    # Displays readable label names ("Male"/"Female") on reads but takes short keys ("M"/"F") on writes
    gender_display = serializers.CharField(source='get_gender_display', read_only=True)

    class Meta:
        model = Patient
        fields = ['id', 'first_name', 'last_name', 'date_of_birth', 'gender', 'gender_display', 'phone_number', 'email', 'address', 'medical_history', 'created_at']


"""
from rest_framework import serializers
from .models import Patient

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

        """