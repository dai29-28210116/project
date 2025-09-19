from django.urls import path
from core.views.menu import UserMenuListAPIView

urlpatterns = [
    path("menus/", UserMenuListAPIView.as_view(), name="user-menus"),
]
