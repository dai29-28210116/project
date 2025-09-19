# core/serializers/menu.py
from rest_framework import serializers
from core.models.menu import Menu

class MenuSerializer(serializers.ModelSerializer):
    children = serializers.SerializerMethodField()

    class Meta:
        model = Menu
        fields = ["code", "title", "icon", "path", "children"]

    def get_children(self, obj):
        return MenuSerializer(obj.children.all(), many=True).data