from rest_framework import viewsets, permissions
from notice.models.notice_category import NoticeCategory
from notice.serializers.category import NoticeCategorySerializer


class NoticeCategoryViewSet(viewsets.ModelViewSet):
    queryset = NoticeCategory.objects.all()
    serializer_class = NoticeCategorySerializer
    permission_classes = [permissions.IsAuthenticated]