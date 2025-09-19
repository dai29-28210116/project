from rest_framework import viewsets, permissions
from django.utils.timezone import now
from notice.models.notice import Notice
from notice.models.notice_category import NoticeCategory
from notice.serializers.notice import NoticeSerializer, NoticeCategorySerializer

class NoticeViewSet(viewsets.ModelViewSet):
    serializer_class = NoticeSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        today = now().date()
        qs = Notice.objects.filter(
            publish_from__lte=today,
            publish_to__gte=today
        ).prefetch_related("categories", "departments")
        user = self.request.user
        if not user.is_staff:
            qs = qs.filter(
                departments__code__in=user.userdept_set.values("dept_id")
            )

        return qs.distinct()

class NoticeCategoryViewSet(viewsets.ModelViewSet):
    queryset = NoticeCategory.objects.all()
    serializer_class = NoticeCategorySerializer
    permission_classes = [permissions.IsAuthenticated]