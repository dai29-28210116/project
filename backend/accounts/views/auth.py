from django.contrib.auth import authenticate, login, logout
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from ..serializers.auth import LoginSerializer
from ..models import UserDept, UserRole

class LoginView(APIView):
    permission_classes = []  # 未ログインでも使える

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = authenticate(
            request,
            username=serializer.validated_data["username"],
            password=serializer.validated_data["password"],
        )
        if user is not None:
            login(request, user)
            return Response({"message": "ログイン成功"})
        return Response({"error": "認証失敗"}, status=status.HTTP_401_UNAUTHORIZED)


class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "ログアウトしました"})


class AuthStatusView(APIView):
    def get(self, request):
        if request.user.is_authenticated:
            departments = [
                {"code": ud.dept.code, "name": ud.dept.name}
                for ud in UserDept.objects.filter(user=request.user)
            ]
            roles = [ur.role.code for ur in UserRole.objects.filter(user=request.user)]
            return Response({
                "username": request.user.username,
                "full_name": request.user.full_name,
                "is_staff": request.user.is_staff,
                "departments": departments,
                "roles": roles,
            })
        return Response({"authenticated": False}, status=status.HTTP_401_UNAUTHORIZED)