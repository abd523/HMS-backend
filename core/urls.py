from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from billing.views import InvoiceViewSet, ReportAnalyticsView
from pharmacy.views import MedicineViewSet
from laboratory.views import LabRequestViewSet, LabTestViewSet
from appointments.views import AppointmentViewSet
from patients.views import PatientViewSet
from doctors.views import DoctorViewSet
from notifications.views import NotificationViewSet
# Imported the missing clinical framework modules
from prescriptions.views import MedicalRecordViewSet, PrescriptionViewSet 

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet, basename='invoice')
router.register(r'medicines', MedicineViewSet, basename='medicine')
router.register(r'lab-requests', LabRequestViewSet, basename='lab-request')
router.register(r'lab-tests', LabTestViewSet, basename='lab-test')
router.register(r'appointments', AppointmentViewSet, basename='appointment')
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'notifications', NotificationViewSet, basename='notification')
# Grade 6 fix: Registered missing viewsets into the central routing network map
router.register(r'records', MedicalRecordViewSet, basename='medical-record')
router.register(r'prescriptions', PrescriptionViewSet, basename='prescription')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/reports/analytics/', ReportAnalyticsView.as_view(), name='report-analytics'),
    path('api/', include(router.urls)),
]



"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from billing.views import InvoiceViewSet, ReportAnalyticsView
from pharmacy.views import MedicineViewSet
from laboratory.views import LabRequestViewSet, LabTestViewSet
from appointments.views import AppointmentViewSet
from patients.views import PatientViewSet
from doctors.views import DoctorViewSet
from notifications.views import NotificationViewSet

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet, basename='invoice')
router.register(r'medicines', MedicineViewSet, basename='medicine')
router.register(r'lab-requests', LabRequestViewSet, basename='lab-request')
router.register(r'lab-tests', LabTestViewSet, basename='lab-test')
router.register(r'appointments', AppointmentViewSet, basename='appointment')
router.register(r'patients', PatientViewSet, basename='patient')
router.register(r'doctors', DoctorViewSet, basename='doctor')
router.register(r'notifications', NotificationViewSet, basename='notification')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('accounts.urls')),
    path('api/reports/analytics/', ReportAnalyticsView.as_view(), name='report-analytics'),
    path('api/', include(router.urls)),
]

"""