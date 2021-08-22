from django.db import models
from django.utils.translation import ugettext_lazy as _
from uuid import uuid4


class AbstractUUID(models.Model):
    uuid = models.UUIDField(
        primary_key=True,
        default=uuid4,
        unique=True,
        editable=False,
        verbose_name=_('utils.base_model.uuid')
    )

    class Meta:
        abstract = True
        ordering = ('uuid', )


class AbstractTimeTracker(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('utils.model_date.created_at')
    )
    updated_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_('utils.model_date.updated_at')
    )

    class Meta:
        abstract = True
        ordering = ('updated_at', 'created_at')
