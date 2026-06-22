from rest_framework import viewsets, filters, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth

from .models import Invoice
from .serializers import InvoiceSerializer
from patients.models import Patient
from accounts.models import AuditLog

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('-created_at')
    serializer_class = InvoiceSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'patient']
    search_fields = ['patient__first_name', 'patient__last_name']

    def perform_update(self, serializer):
        # Grade 6 rule: Check if bill is getting paid, then record it in the ledger!
        old_status = self.get_object().status
        invoice = serializer.save()
        
        if old_status == 'Unpaid' and invoice.status == 'Paid':
            AuditLog.objects.create(
                user=self.request.user if self.request.user.is_authenticated else None,
                action=f"Collected Payment of {invoice.total_amount} Birr for Invoice #{invoice.id}"
            )

class ReportAnalyticsView(APIView):
    permission_classes = [permissions.IsAdminUser]

    def get(self, request):
        monthly_revenue = (
            Invoice.objects.filter(status='Paid')
            .annotate(month=TruncMonth('created_at'))
            .values('month')
            .annotate(total=Sum('total_amount'))
            .order_by('month')
        )

        gender_stats = Patient.objects.values('gender').annotate(count=Count('id'))

        # Safe parsing adjustments preventing crashes on null data arrays
        revenue_trend = []
        for item in monthly_revenue:
            if item["month"] and item["total"]:
                revenue_trend.append({
                    "month": item["month"].strftime("%B"),
                    "amount": float(item["total"])
                })

        gender_demographics = []
        for item in gender_stats:
            gender_label = "Unknown"
            if item["gender"] == "M":
                gender_label = "Male"
            elif item["gender"] == "F":
                gender_label = "Female"
            
            gender_demographics.append({
                "gender": gender_label,
                "count": item["count"]
            })

        return Response({
            "revenue_trend": revenue_trend,
            "gender_demographics": gender_demographics,
        })







"""

from rest_framework import viewsets, filters, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Sum, Count
from django.db.models.functions import TruncMonth

from .models import Invoice
from .serializers import InvoiceSerializer
from patients.models import Patient


class InvoiceViewSet(viewsets.ModelViewSet):
    queryset = Invoice.objects.all().order_by('-created_at')
    serializer_class = InvoiceSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    filterset_fields = ['status', 'patient']
    search_fields = ['patient__first_name', 'patient__last_name']


class ReportAnalyticsView(APIView):
    permission_classes = [permissions.IsAdminUser]  # አስተዳዳሪዎች ብቻ እንዲያዩት

    def get(self, request):
        # 1. የወርሃዊ ገቢ ትንታኔ (Monthly Revenue Breakdown)
        monthly_revenue = (
            Invoice.objects.filter(status='Paid')
            .annotate(month=TruncMonth('created_at'))
            .values('month')
            .annotate(total=Sum('total_amount'))
            .order_by('month')
        )

        # 2. የታካሚዎች ስርጭት በጾታ (Patient Gender Distribution)
        gender_stats = Patient.objects.values('gender').annotate(count=Count('id'))

        # 3. አጠቃላይ የሆስፒታሉ አፈፃፀም ማጠቃለያ
        report_data = {
            "revenue_trend": [
                {
                    "month": item["month"].strftime("%B"),
                    "amount": float(item["total"])
                }
                for item in monthly_revenue
            ],
            "gender_demographics": [
                {
                    "gender": "Male" if item["gender"] == "M" else "Female",
                    "count": item["count"]
                }
                for item in gender_stats
            ],
        }

        return Response(report_data)


        """