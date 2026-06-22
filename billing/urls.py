from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import InvoiceViewSet, ReportAnalyticsView

router = DefaultRouter()
router.register(r'invoices', InvoiceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('analytics/reports/', ReportAnalyticsView.as_view(), name='billing-analytics'),
]