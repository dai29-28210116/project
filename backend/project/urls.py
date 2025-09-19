# project/urls.py
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/accounts/", include("accounts.urls")),  
    path("api/core/", include("core.urls")),          
    path("api/notice/", include("notice.urls")),
]