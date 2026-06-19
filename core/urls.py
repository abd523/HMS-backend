from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

# ቪውሴቶችን ከየአፖቻቸው አምጥተናል
from billing.views import InvoiceViewSet
from pharmacy.views import MedicineViewSet
from laboratory.views import LabRequestViewSet, LabTestViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet, basename='invoice')
router.register(r'medicines', MedicineViewSet, basename='medicine')
router.register(r'lab-requests', LabRequestViewSet, basename='lab-request')
router.register(r'lab-tests', LabTestViewSet, basename='lab-test')

urlpatterns = [
    path('admin/', admin.site.urls),

    # Accounts API (users, login, refresh)
    path('api/', include('accounts.urls')),

    # Other API endpoints
    path('api/', include(router.urls)),
]
