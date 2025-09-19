from django.db import models
from django.contrib.auth import get_user_model
from accounts.models.dept import Dept
from .notice_category import NoticeCategory

User = get_user_model()

class Notice(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()  # HTML (QuillEditor 入力)

    publish_from = models.DateField()
    publish_to = models.DateField()

    departments = models.ManyToManyField(Dept, related_name="notices")
    categories = models.ManyToManyField(NoticeCategory, related_name="notices")

    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-publish_from"]

    def __str__(self):
        return self.title