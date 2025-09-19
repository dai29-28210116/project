# core/models/attachments.py
import os
from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from accounts.models.user import User

def attachment_upload_path(instance, filename):
    app_label = instance.content_type.app_label
    section = instance.section or 'default'
    return os.path.join('attachments', app_label, section, filename)

class Attachment(models.Model):
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    section = models.CharField(max_length=100, verbose_name="セクション識別子")
    file = models.FileField(upload_to=attachment_upload_path)
    original_name = models.CharField(max_length=200, blank=True)
    uploaded_by = models.ForeignKey(User, on_delete=models.PROTECT, null=True, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-uploaded_at']

    def __str__(self):
        return f"{self.section} / {self.file.name}"