from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from django.db.models import Sum

from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from billing.models import Invoice
from .models import AuditLog
from .serializers import UserSerializer

User = get_user_model()

class CustomTokenObtainPairView(TokenObtainPairView):
    pass

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # Refactored: Admin manages everything, but authenticated users can read basic details
    permission_classes = [permissions.IsAuthenticated] 

class DashboardStatsView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        total_patients = Patient.objects.count()
        total_doctors = Doctor.objects.count()
        total_appointments = Appointment.objects.count()
        
        # Fixed duplicate line debt
        total_revenue = Invoice.objects.filter(status='Paid').aggregate(Sum('total_amount'))['total_amount__sum'] or 0
        
        # Real Live Audit Logs from database instead of fake hardcoded arrays!
        logs = AuditLog.objects.all()[:5]
        recent_activities = [{"id": log.id, "message": f"{log.user.username if log.user else 'System'}: {log.action}"} for log in logs]

        data = {
            "total_patients": total_patients,
            "total_doctors": total_doctors,
            "total_appointments": total_appointments,
            "total_revenue": float(total_revenue),
            "recent_activities": recent_activities
        }
        return Response(data)




"""
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView
from django.contrib.auth import get_user_model
from django.db.models import Sum

# የሌሎች አፖችን ሞዴሎች ማስገባት (Imports)
from patients.models import Patient
from doctors.models import Doctor
from appointments.models import Appointment
from billing.models import Invoice

from .serializers import UserSerializer

User = get_user_model()


# Custom Login View (ከተጠቃሚው Role ጋር አብሮ ለመመለስ)
class CustomTokenObtainPairView(TokenObtainPairView):
    # እዚህ ላይ ተጨማሪ የቶክን መረጃ ማበጀት ይቻላል (አማራጭ)
    pass


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]  # ለጊዜው Admin ብቻ CRUD እንዲያደርግ


# 1. አዲሱ የዳሽቦርድ መረጃ ሰብሳቢ View እዚህ ጋር ተጨምሯል
class DashboardStatsView(APIView):
    permission_classes = [permissions.IsAuthenticated] # ሎጊን ያደረገ ተጠቃሚ ብቻ እንዲያየው

    def get(self, request):
        total_patients = Patient.objects.count()
        total_doctors = Doctor.objects.count()
        total_appointments = Appointment.objects.count()
        #total_revenue = Invoice.objects.filter(status='Paid').aggregate(Sum('total_amount'))['total_amount__sum'] or 0
        total_revenue = Invoice.objects.filter(status='Paid').aggregate(Sum('total_amount'))['total_amount__sum'] or 0
        data = {
            "total_patients": total_patients,
            "total_doctors": total_doctors,
            "total_appointments": total_appointments,
            "total_revenue": float(total_revenue),
            "recent_activities": [
                {"id": 1, "message": "New patient registered"},
                {"id": 2, "message": "Appointment scheduled with Dr. Yohannes"}
            ]
        }
        return Response(data)
        """