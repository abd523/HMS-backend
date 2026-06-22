"""from django.contrib import admin

# Register your models here.
"""

# thsi is the new adde feature 

from django.contrib import admin
from .models import Doctor

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_name', 'specialization', 'license_number', 'experience_years', 'is_available')
    list_filter = ('specialization', 'is_available')
    search_fields = ('user__first_name', 'user__last_name', 'license_number')

    # Helper method to display full name nicely inside Django Admin dashboard
    def get_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    get_name.short_description = 'Doctor Name'