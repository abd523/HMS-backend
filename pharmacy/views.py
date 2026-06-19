from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Medicine
from .serializers import MedicineSerializer

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all().order_by('name')
    serializer_class = MedicineSerializer
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'category']