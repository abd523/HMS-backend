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