"""
from django.test import TestCase

# Create your tests here.
"""

# this is the new added feature
from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Notification

User = get_user_model()

class NotificationTestCase(TestCase):

    def setUp(self):
        self.user1 = User.objects.create_user(username="patient_dawit", password="password123")
        self.user2 = User.objects.create_user(username="dr_meron", password="password123")
        
        # Create a sample message row container
        Notification.objects.create(user=self.user1, title="Test 1", message="Hello Dawit", is_read=False)

    def test_users_cannot_access_others_notifications(self):
        """ Grade 6 safety verification: Ensure user 2 cannot peek inside user 1's mail box! """
        # Force system login state simulation as Doctor Meron (User 2)
        self.client.login(username="dr_meron", password="password123")
        
        # Pull notifications via API simulation call
        response = self.client.get('/api/notifications/')
        
        # Doctor Meron should see 0 items because the test notification belongs only to Dawit!
        self.assertEqual(len(response.data or []), 0)