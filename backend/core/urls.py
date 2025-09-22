# core/api/urls.py
from django.urls import path
from rest_framework import routers
from core.views.menu import UserMenuListAPIView
from core.views.attachment import AttachmentViewSet
from core.views.content_type import ContentTypeListView

router = routers.DefaultRouter()
router.register(r"attachments", AttachmentViewSet)

urlpatterns = [
    path("menus/", UserMenuListAPIView.as_view(), name="user-menus"),
    path("content-types/", ContentTypeListView.as_view(), name="content_type_list"),
]

urlpatterns += router.urls