import uuid
from django.db import models
from django.conf import settings
from django.utils import timezone


class SoftDeleteManager(models.Manager):
    """Hide soft-deleted records by default."""
    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class TrackingModel(models.Model):
    """
    Abstract base model:
    - UUID primary key
    - timestamps
    - soft delete
    - user tracking
    """

    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )

    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    deleted_at = models.DateTimeField(null=True, blank=True, db_index=True)

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_created"
    )

    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="%(class)s_updated"
    )

    objects = models.Manager()
    active_objects = SoftDeleteManager()

    class Meta:
        abstract = True

    def soft_delete(self, user=None):
        self.deleted_at = timezone.now()

        if user:
            self.updated_by = user

        self.save()