# thsi was empty and this folder and file not created at first

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MedicalRecordViewSet, PrescriptionViewSet

router = DefaultRouter()
router.register(r'records', MedicalRecordViewSet)
router.register(r'prescriptions', PrescriptionViewSet)

urlpatterns = [
    path('', include(router.urls)),
]