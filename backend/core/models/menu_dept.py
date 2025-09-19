from django.db import models
from accounts.models.dept import Dept
from core.models.menu import Menu

class MenuDept(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    dept = models.ForeignKey(Dept, on_delete=models.CASCADE)

    class Meta:
        unique_together = ("menu", "dept")

    def __str__(self):
        return f"{self.dept.name} - {self.menu.title}"