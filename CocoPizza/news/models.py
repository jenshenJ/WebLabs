from django.db import models
from django.urls import reverse
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)

    def str(self):
        return self.title

    def get_absolute_url(self):
        return reverse("article", args=[str(self.id)])