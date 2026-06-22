from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Notification
from .serializers import NotificationSerializer

class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Users can only look inside their own personal inbox rows!
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        # Grade 6 rule: Automate user mapping. The system seals the logged-in user right onto the notice.
        serializer.save(user=self.request.user)

    # Grade 6 rule: A fast button that takes all unread mail piles and marks them read in 1 second!
    @action(detail=False, methods=['post'], url_path='mark-all-read')
    def mark_all_read(self, request):
        unread_notifications = self.get_queryset().filter(is_read=False)
        count = unread_notifications.count()
        unread_notifications.update(is_read=True) # Ultra fast batch update execution
        
        return Response(
            {"message": f"Successfully marked {count} notifications as read."}, 
            status=status.HTTP_200_OK
        )



"""
from rest_framework import viewsets, permissions
from .models import Notification
from .serializers import NotificationSerializer


class NotificationViewSet(viewsets.ModelViewSet):
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Notification.objects.filter(user=self.request.user).order_by('-created_at')
"""



