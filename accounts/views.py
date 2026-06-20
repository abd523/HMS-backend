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