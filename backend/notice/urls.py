# notice/urls.py
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from notice.views.notice import NoticeViewSet, NoticeCategoryViewSet

router = DefaultRouter()
router.register(r'notices', NoticeViewSet, basename='notice')  
router.register(r'categories', NoticeCategoryViewSet, basename='notice-category')

urlpatterns = [
    path('', include(router.urls)),
]