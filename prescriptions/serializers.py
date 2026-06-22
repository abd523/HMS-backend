from rest_framework import serializers
from .models import MedicalRecord, Prescription

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'

class MedicalRecordSerializer(serializers.ModelSerializer):
    patient_name = serializers.ReadOnlyField(source='patient.first_name')
    doctor_name = serializers.ReadOnlyField(source='doctor.__str__')
    
    # Nested prescription data block
    prescription = PrescriptionSerializer(read_only=True)

    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient', 'patient_name', 'doctor', 'doctor_name', 'diagnosis', 'doctor_notes', 'prescription', 'created_at']


"""
from rest_framework import serializers
from .models import MedicalRecord, Prescription

class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'


class MedicalRecordSerializer(serializers.ModelSerializer):
    # የታካሚውን እና የሐኪሙን ስም በጽሑፍ ለማየት (ReadOnly)
    patient_name = serializers.ReadOnlyField(source='patient.first_name')
    doctor_name = serializers.ReadOnlyField(source='doctor.user.first_name')
    
    # ከዚህ የሕክምና ታሪክ ጋር የተያያዘውን የመድኃኒት ማዘዣ አብሮ ለማሳየት
    prescription = PrescriptionSerializer(read_only=True)

    class Meta:
        model = MedicalRecord
        fields = ['id', 'patient', 'patient_name', 'doctor', 'doctor_name', 'diagnosis', 'doctor_notes', 'prescription', 'created_at']

        """