from django.db import models
from accounts.models.dept import Dept  # 部署マスタ

class Menu(models.Model):
    code = models.CharField(max_length=50, unique=True)
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=50, blank=True)
    path = models.CharField(max_length=200, blank=True)  # Vue Router の path
    parent = models.ForeignKey(
        "self", null=True, blank=True, related_name="children", on_delete=models.CASCADE
    )

    def __str__(self):
        return self.title