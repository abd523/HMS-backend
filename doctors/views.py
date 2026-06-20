from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Doctor
from .serializers import DoctorSerializer

class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all().order_by('id')
    serializer_class = DoctorSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['specialization', 'is_available']
    search_fields = ['user__first_name', 'user__last_name', 'specialization']