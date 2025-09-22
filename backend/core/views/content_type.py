# core/api/views/content_type.py
from rest_framework import generics
from django.contrib.contenttypes.models import ContentType
from core.serializers.content_type import ContentTypeSerializer


class ContentTypeListView(generics.ListAPIView):
    serializer_class = ContentTypeSerializer

    def get_queryset(self):
        """
        ?model=notice のようにクエリで絞り込み可能
        """
        qs = ContentType.objects.all()
        model = self.request.query_params.get("model")
        if model:
            qs = qs.filter(model=model)
        return qs
