"""

from django.contrib import admin

# Register your models here.
"""

# thsi is the new adde feature 

from django.contrib import admin
from .models import LabRequest, LabTest

@admin.register(LabRequest)
class LabRequestAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'doctor', 'test_name', 'status', 'created_at')
    list_filter = ('status', 'created_at')

@admin.register(LabTest)
class LabTestAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'test_name', 'status', 'ordered_at', 'completed_at')
    list_filter = ('status', 'ordered_at')