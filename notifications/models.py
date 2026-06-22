# thsi is the new added feature

from django.db import models
from django.conf import settings
from django.core.exceptions import ValidationError

class Notification(models.Model):
    # Grade 6 rule: CASCADE is perfect here because if a user profile is deleted, their old alerts can safely vanish.
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    
    # Grade 6 tip: db_index=True creates an invisible bookmark tab so Django can find unread alerts instantly!
    is_read = models.BooleanField(default=False, db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        # Newest alerts show up at the top of the tray automatically!
        ordering = ['-created_at']

    def clean(self):
        # Grade 6 rule: Block notifications that say absolutely nothing!
        if self.title and not self.title.strip():
            raise ValidationError("Notification title cannot be empty text space.")
        if self.message and not self.message.strip():
            raise ValidationError("Notification message cannot be empty text space.")

    def save(self, *args, **kwargs):
        self.full_clean() # Forces our clean rules to run automatically before saving
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.title}"


"""
from django.db import models
from django.conf import settings

class Notification(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    title = models.CharField(max_length=255)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Notification for {self.user.username} - {self.title}"

        """