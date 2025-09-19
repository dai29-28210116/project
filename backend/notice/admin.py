from django.contrib import admin
from notice.models.notice_category import NoticeCategory

@admin.register(NoticeCategory)
class NoticeCategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    search_fields = ("name",)