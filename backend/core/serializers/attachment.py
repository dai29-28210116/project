# core/api/serializers/attachment.py
from rest_framework import serializers
from core.models.attachments import Attachment

class AttachmentSerializer(serializers.ModelSerializer):
    uploaded_by = serializers.StringRelatedField(read_only=True)
    original_filename = serializers.SerializerMethodField()
    content_type_id = serializers.PrimaryKeyRelatedField(
        source="content_type",
        queryset=Attachment._meta.get_field("content_type").remote_field.model.objects.all(),
        write_only=True
    )
    content_type = serializers.StringRelatedField(read_only=True)

    def get_original_filename(self, obj):
        # original_name があればそれを使い、なければ file.name の末尾を返す
        return obj.original_name or obj.file.name.split("/")[-1]

    class Meta:
        model = Attachment
        fields = [
            "id",
            "file",
            "original_filename",
            "content_type",      # ← レスポンス用 (人間可読)
            "content_type_id",   # ← リクエスト用 (数値ID)
            "object_id",
            "section",
            "uploaded_by",
            "uploaded_at",
        ]
        read_only_fields = ["uploaded_by", "uploaded_at"]
