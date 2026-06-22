from django.contrib import admin
from .models import Medicine

@admin.register(Medicine)
class MedicineAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'quantity_in_stock', 'price_per_unit', 'expiry_date', 'is_expired')
    list_filter = ('category', 'expiry_date')
    search_fields = ('name', 'category')


"""
from django.contrib import admin

# Register your models here.
"""
