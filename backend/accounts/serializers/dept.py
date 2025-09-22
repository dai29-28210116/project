from rest_framework import serializers
from accounts.models.dept import Dept


class DeptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dept
        fields = ["id", "code", "name"]