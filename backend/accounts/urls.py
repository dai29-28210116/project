from django.urls import path
from .views.auth import LoginView, LogoutView, AuthStatusView

urlpatterns = [
    path("auth/login/", LoginView.as_view(), name="login"),
    path("auth/logout/", LogoutView.as_view(), name="logout"),
    path("auth/status/", AuthStatusView.as_view(), name="auth_status"),
]