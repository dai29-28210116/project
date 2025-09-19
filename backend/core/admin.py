from django.contrib import admin
from core.models import Menu, MenuDept

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ("code", "title", "path", "parent")
    search_fields = ("code", "title")

@admin.register(MenuDept)
class MenuDeptAdmin(admin.ModelAdmin):
    list_display = ("menu", "dept")
    list_filter = ("dept",)