from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    # የታካሚውን እና የሐኪሙን ስም በጽሑፍ ጭምር ለማየት (አማራጭ ግን ጠቃሚ)
    patient_name = serializers.ReadOnlyField(source='patient.first_name')
    doctor_name = serializers.ReadOnlyField(source='doctor.user.first_name')

    class Meta:
        model = Appointment
        fields = '__all__' # ሁሉንም የሞዴል ፊልዶች ያካትታል