from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Appointment
from .serializers import AppointmentSerializer
from accounts.models import AuditLog # Importing our audit log block!

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all().order_by('appointment_date', 'appointment_time')
    serializer_class = AppointmentSerializer
    
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'doctor', 'patient'] 
    search_fields = ['reason', 'patient__first_name', 'patient__last_name']

    def perform_create(self, serializer):
        # Grade 6 rule: Automatically write down who did what into the history book
        appointment = serializer.save()
        AuditLog.objects.create(
            user=self.request.user if self.request.user.is_authenticated else None,
            action=f"Booked an appointment for Patient ID #{appointment.patient.id if appointment.patient else 'Unknown'}"
        )






"""
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import Appointment
from .serializers import AppointmentSerializer

class AppointmentViewSet(viewsets.ModelViewSet):
    # ቀጠሮዎችን በቅርብ ቀን እና ሰዓት ቅደም ተከተል ያደራጃል
    queryset = Appointment.objects.all().order_by('appointment_date', 'appointment_time')
    serializer_class = AppointmentSerializer
    
    # የማጣሪያ እና የፍለጋ ዘዴዎች
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'doctor', 'patient'] 
    search_fields = ['reason', 'patient__first_name', 'patient__last_name']

    """