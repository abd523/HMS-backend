from django.contrib import admin
from .models import MedicalRecord, Prescription

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'diagnosis', 'created_at')
    list_filter = ('created_at', 'doctor')
    search_fields = ('patient__first_name', 'patient__last_name', 'diagnosis')

@admin.register(Prescription)
class PrescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'record', 'created_at')

"""
from django.contrib import admin

# Register your models here.
"""