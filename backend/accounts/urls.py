# accounts/api/urls.py
from django.urls import path
from rest_framework import routers
from .views.dept import DeptViewSet
from .views.auth import LoginView, LogoutView, AuthStatusView

router = routers.DefaultRouter()
router.register(r"departments", DeptViewSet)

urlpatterns = [
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("auth/status/", AuthStatusView.as_view(), name="auth_status"),
]

urlpatterns += router.urls
