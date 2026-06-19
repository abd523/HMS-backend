from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
# 1. DashboardStatsView ከቪውስ (views) ውስጥ እንዲመጣ እዚህ ጋር ጨምረነዋል
from .views import CustomTokenObtainPairView, UserViewSet, DashboardStatsView

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    
    # 2. አዲሱ የዳሽቦርድ ስታቲስቲክስ URL መድረሻ እዚህ ጋር ተገንብቷል
    path('dashboard/stats/', DashboardStatsView.as_view(), name='dashboard-stats'),
]