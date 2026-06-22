from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Medicine
from .serializers import MedicineSerializer
from accounts.models import AuditLog

class MedicineViewSet(viewsets.ModelViewSet):
    queryset = Medicine.objects.all().order_by('name')
    serializer_class = MedicineSerializer
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['category']
    search_fields = ['name', 'category']

    def perform_create(self, serializer):
        # Automatically document new supply inputs to the main registry system ledger
        medicine = serializer.save()
        AuditLog.objects.create(
            user=self.request.user if self.request.user.is_authenticated else None,
            action=f"Added new medication stock: {medicine.name} ({medicine.quantity_in_stock} units logged)"
        )


"""
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
    """