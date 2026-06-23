# this folder and file is the new added
import uuid
from django.db import models
from django.conf import settings

class SoftDeleteManager(models.Manager):
    """Custom manager to ensure deleted records don't show up in standard queries."""
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)

class TrackingModel(models.Model):
    # 1. UUID Primary Keys (Highly secure, hides record counts from the frontend URL)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    # 2. Audit Fields (Timestamps)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True) # Index added for fast sorting
    updated_at = models.DateTimeField(auto_now=True)
    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)

    # 3. User Tracking Fields (Foreign Keys with custom constraints)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created" # Prevents namespace collisions dynamically
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated"
    )

    # Core object managers
    objects = models.Manager() # Default manager (includes soft-deleted items for history)
    active_objects = SoftDeleteManager() # Clean manager for daily dashboard views

    class Meta:
        abstract = True # ⚠️ CRITICAL: Tells Django not to create a database table for this class itself.

    def soft_delete(self, user=None):
        """Custom method to soft delete an item without removing it from the database."""
        from django.utils import timezone
        self.deleted_at = timezone.now()
        if user:
            self.updated_by = user
        self.save()