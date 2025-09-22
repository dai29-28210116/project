# core/api/serializers/content_type.py
from rest_framework import serializers
from django.contrib.contenttypes.models import ContentType


class ContentTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContentType
        fields = ["id", "app_label", "model"]
