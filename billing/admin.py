"""
from django.contrib import admin

# Register your models here.
"""

# this feature was not created fist

from django.contrib import admin
from .models import Invoice

@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'patient', 'total_amount', 'status', 'created_at', 'paid_at')
    list_filter = ('status', 'created_at')
    search_fields = ('patient__first_name', 'patient__last_name')