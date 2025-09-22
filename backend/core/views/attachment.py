# core/api/views/attachment.py
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from core.models.attachments import Attachment
from core.serializers.attachment import AttachmentSerializer


class AttachmentViewSet(viewsets.ModelViewSet):
    queryset = Attachment.objects.all()
    serializer_class = AttachmentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        qs = super().get_queryset()
        content_type = self.request.query_params.get("content_type")
        content_type_id = self.request.query_params.get("content_type_id")
        object_id = self.request.query_params.get("object_id")

        if content_type:
            qs = qs.filter(content_type__model=content_type.lower())
        if content_type_id:
            qs = qs.filter(content_type_id=content_type_id)
        if object_id:
            qs = qs.filter(object_id=object_id)

        return qs

    def perform_create(self, serializer):
        serializer.save(uploaded_by=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.uploaded_by != request.user:
            return Response(
                {"detail": "削除できるのはアップロードした本人のみ"},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().destroy(request, *args, **kwargs)