from django.db import models

class NoticeCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    class Meta:
        verbose_name = "お知らせカテゴリ"
        verbose_name_plural = "お知らせカテゴリ"

    def __str__(self):
        return self.name