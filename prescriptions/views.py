from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import MedicalRecord, Prescription
from .serializers import MedicalRecordSerializer, PrescriptionSerializer

class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all().order_by('-created_at')
    serializer_class = MedicalRecordSerializer
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['patient', 'doctor']
    search_fields = ['diagnosis', 'doctor_notes']


class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all().order_by('-created_at')
    serializer_class = PrescriptionSerializer
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['record']
    # Removed raw text medications search to avoid severe JSON runtime database crashes
    search_fields = ['record__id', 'record__patient__first_name', 'record__patient__last_name']


"""
from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import MedicalRecord, Prescription
from .serializers import MedicalRecordSerializer, PrescriptionSerializer

# Create your views here.

# 1. የታካሚዎች የሕክምና ታሪክ (EMR) እይታ
class MedicalRecordViewSet(viewsets.ModelViewSet):
    queryset = MedicalRecord.objects.all().order_by('-created_at')
    serializer_class = MedicalRecordSerializer
    
    # የማጣሪያ እና የፍለጋ ዘዴዎች
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['patient', 'doctor']
    search_fields = ['diagnosis', 'doctor_notes']


# 2. የታዘዙ መድኃኒቶች (Prescription) እይታ
class PrescriptionViewSet(viewsets.ModelViewSet):
    queryset = Prescription.objects.all().order_by('-created_at')
    serializer_class = PrescriptionSerializer
    
    # ማጣሪያ
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['record']
    search_fields = ['medications'] # በታዘዙት መድኃኒቶች ስም ለመፈለግ

    """