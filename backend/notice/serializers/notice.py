# notice/api/serializers/notice.py
from rest_framework import serializers
from notice.models.notice import Notice
from accounts.models.dept import Dept
from notice.models.notice_category import NoticeCategory
from accounts.serializers.dept import DeptSerializer
from notice.serializers.category import NoticeCategorySerializer
from core.models.attachments import Attachment
from core.serializers.attachment import AttachmentSerializer


class NoticeSerializer(serializers.ModelSerializer):
    # レスポンス用（オブジェクト配列）
    departments = DeptSerializer(many=True, read_only=True)
    categories = NoticeCategorySerializer(many=True, read_only=True)
    attachments = serializers.SerializerMethodField()  # ← 添付ファイルを追加

    # 書き込み用（ID配列）
    department_ids = serializers.PrimaryKeyRelatedField(
        queryset=Dept.objects.all(), many=True, write_only=True, source="departments"
    )
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=NoticeCategory.objects.all(), many=True, write_only=True, source="categories"
    )

    class Meta:
        model = Notice
        fields = [
            "id",
            "title",
            "content",
            "publish_from",
            "publish_to",
            "departments",      # GET時のオブジェクト配列
            "categories",       # GET時のオブジェクト配列
            "department_ids",   # POST/PUT時のID配列
            "category_ids",     # POST/PUT時のID配列
            "attachments",      # 添付ファイル一覧
            "created_by",
            "created_at",
        ]
        read_only_fields = ["created_by", "created_at"]

    def get_attachments(self, obj):
        qs = Attachment.objects.filter(
            content_type__model="notice",
            object_id=obj.id,
        ).order_by("-uploaded_at")
        return AttachmentSerializer(qs, many=True, context=self.context).data
