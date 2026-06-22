"""
from django.contrib import admin

# Register your models here.
"""

# this is the new added feature 

from django.contrib import admin
from .models import Patient

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'phone_number', 'created_at')
    list_filter = ('gender', 'created_at')
    search_fields = ('first_name', 'last_name', 'phone_number', 'email')