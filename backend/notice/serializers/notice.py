from rest_framework import serializers
from notice.models.notice import Notice
from notice.models.notice_category import NoticeCategory

class NoticeCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NoticeCategory
        fields = ["id", "name"]


class NoticeSerializer(serializers.ModelSerializer):
    # 読み取り用（詳細や一覧でカテゴリ名を返す）
    categories = NoticeCategorySerializer(many=True, read_only=True)

    # 書き込み用（登録・更新時はIDリストを受け取る）
    category_ids = serializers.PrimaryKeyRelatedField(
        queryset=NoticeCategory.objects.all(),
        many=True,
        write_only=True,
        source="categories"
    )
    department_ids = serializers.PrimaryKeyRelatedField(
        queryset=Notice._meta.get_field("departments").remote_field.model.objects.all(),
        many=True,
        write_only=True,
        source="departments"
    )

    class Meta:
        model = Notice
        fields = [
            "id", "title", "content",
            "publish_from", "publish_to",
            "categories", "category_ids",
            "departments", "department_ids",
            "created_by", "created_at"
        ]
        read_only_fields = ["id", "created_by", "created_at"]

    def validate(self, data):
        """公開期間の整合性チェック"""
        publish_from = data.get("publish_from")
        publish_to = data.get("publish_to")
        if publish_from and publish_to and publish_from > publish_to:
            raise serializers.ValidationError("公開期間が不正です（開始日が終了日より後になっています）")

        # 本文チェック（QuillEditor だと <p><br></p> のみが入るケースもある）
        content = data.get("content", "").strip()
        if not content or content in ["<p><br></p>", "<p></p>"]:
            raise serializers.ValidationError("本文を入力してください")

        return data

    def create(self, validated_data):
        """作成時に自動で作成者をセット"""
        validated_data["created_by"] = self.context["request"].user
        return super().create(validated_data)