# core/views/menu.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from core.models import Menu
from core.serializers.menu import MenuSerializer

class UserMenuListAPIView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        # ユーザー所属部署コードを取得
        departments = request.user.userdept_set.values_list("dept__code", flat=True)

        # 部署に紐付くメニューを取得（root のみ）
        menus = Menu.objects.filter(
            menudept__dept__code__in=departments, parent__isnull=True
        ).distinct()

        serializer = MenuSerializer(menus, many=True)
        return Response(serializer.data)