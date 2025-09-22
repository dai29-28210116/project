from rest_framework import viewsets, permissions
from accounts.models.dept import Dept
from accounts.serializers.dept import DeptSerializer


class DeptViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Dept.objects.all()
    serializer_class = DeptSerializer
    permission_classes = [permissions.IsAuthenticated]