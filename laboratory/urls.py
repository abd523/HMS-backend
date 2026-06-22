# this was empty

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import LabRequestViewSet, LabTestViewSet

router = DefaultRouter()
router.register(r'requests', LabRequestViewSet)
router.register(r'tests', LabTestViewSet)

urlpatterns = [
    path('', include(router.urls)),
]