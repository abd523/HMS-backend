from rest_framework import serializers
from .models import Doctor
from accounts.serializers import UserSerializer
from django.contrib.auth import get_user_model

User = get_user_model()

class DoctorSerializer(serializers.ModelSerializer):   
    # This displays the full user details when reading (GET)
    user_details = UserSerializer(source='user', read_only=True)
    
    # This allows passing a simple User ID number when creating/updating (POST/PUT)
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())

    class Meta:
        model = Doctor
        fields = ['id', 'user', 'user_details', 'specialization', 'license_number', 'experience_years', 'is_available']



"""
from rest_framework import serializers
from .models import Doctor
from accounts.serializers import UserSerializer

class DoctorSerializer(serializers.ModelSerializer):   
    user = UserSerializer(read_only=True) # የተጠቃሚውን ስምና ኢሜይል አብሮ ለማውጣት

    class Meta:
        model = Doctor
        fields = '__all__'


        """