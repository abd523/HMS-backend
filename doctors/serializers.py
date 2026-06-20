from rest_framework import serializers
from .models import Doctor
from accounts.serializers import UserSerializer

class DoctorSerializer(serializers.ModelSerializer):   
    user = UserSerializer(read_only=True) # የተጠቃሚውን ስምና ኢሜይል አብሮ ለማውጣት

    class Meta:
        model = Doctor
        fields = '__all__'