from rest_framework import serializers
from ..models.notice_category import NoticeCategory


class NoticeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeCategory
        fields = ["id", "name"]