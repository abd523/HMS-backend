from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.ReadOnlyField(source='patient.first_name')
    # fallback to just doctor profile string if user mapping is different
    doctor_name = serializers.ReadOnlyField(source='doctor.__str__') 

    class Meta:
        model = Appointment
        fields = '__all__'

    def validate(self, data):
        # Grade 6 rule: Let's make sure the doctor isn't busy at that exact same hour!
        doctor = data.get('doctor')
        date = data.get('appointment_date')
        time = data.get('appointment_time')

        # Check if an existing active appointment overlaps
        clash_exists = Appointment.objects.filter(
            doctor=doctor,
            appointment_date=date,
            appointment_time=time,
            status__in=['Pending', 'Confirmed']
        ).exists()

        if clash_exists:
            raise serializers.ValidationError("This doctor is already booked at this specific date and time!")
        
        return data





"""
from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    # የታካሚውን እና የሐኪሙን ስም በጽሑፍ ጭምር ለማየት (አማራጭ ግን ጠቃሚ)
    patient_name = serializers.ReadOnlyField(source='patient.first_name')
    doctor_name = serializers.ReadOnlyField(source='doctor.user.first_name')

    class Meta:
        model = Appointment
        fields = '__all__' # ሁሉንም የሞዴል ፊልዶች ያካትታል

        """