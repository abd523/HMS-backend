from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import LabRequest, LabTest
from .serializers import LabRequestSerializer, LabTestSerializer

class LabRequestViewSet(viewsets.ModelViewSet):
    queryset = LabRequest.objects.all().order_by('-created_at')
    serializer_class = LabRequestSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'patient', 'doctor']
    search_fields = ['test_name']

class LabTestViewSet(viewsets.ModelViewSet):
    queryset = LabTest.objects.all().order_by('-ordered_at')
    serializer_class = LabTestSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'patient']
    search_fields = ['test_name', 'test_result']




"""
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import LabRequest, LabTest
from .serializers import LabRequestSerializer, LabTestSerializer

class LabRequestViewSet(viewsets.ModelViewSet):
    queryset = LabRequest.objects.all().order_by('-created_at')
    serializer_class = LabRequestSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'patient']
    search_fields = ['test_name']

class LabTestViewSet(viewsets.ModelViewSet):
    queryset = LabTest.objects.all().order_by('-ordered_at')
    serializer_class = LabTestSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'patient']
    search_fields = ['test_name', 'test_result']


    """