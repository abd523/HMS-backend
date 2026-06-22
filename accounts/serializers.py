from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'phone_number', 'password', 'is_approved']
        extra_kwargs = {
            'password': {'write_only': True, 'required': False},
            'is_approved': {'read_only': True} # Patients can't approve themselves!
        }

    def create(self, validated_data):
        # Securely create user with a hashed password
        user = User.objects.create_user(**validated_data)
        return user

    def update(self, instance, validated_data):
        # Securely update user details and handle new password if changed
        password = validated_data.pop('password', None)
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        if password:
            instance.set_password(password)
        instance.save()
        return instance










"""
from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
        """