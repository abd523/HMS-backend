# the new feature totally this was not created before

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AppointmentViewSet

router = DefaultRouter()
router.register(r'', AppointmentViewSet) # Mounts the endpoints cleanly

urlpatterns = [
    path('', include(router.urls)),
]