# accounts/models/dept.py
from django.db import models

class Dept(models.Model):
    code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.code} {self.name}"