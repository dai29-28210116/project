from rest_framework import viewsets, permissions
from django.utils.timezone import now
from notice.models.notice import Notice
from notice.serializers.notice import NoticeSerializer

class NoticeViewSet(viewsets.ModelViewSet):
    queryset = Notice.objects.all().prefetch_related("departments", "categories")
    serializer_class = NoticeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.created_by != request.user and not request.user.is_staff:
            return Response(
                {"detail": "削除できるのは作成者または管理者のみ"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)
    