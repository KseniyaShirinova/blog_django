from typing import Text
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.db.models.fields.related import ForeignKey, create_many_to_many_intermediary_model

class Post(models.Model):
    author = ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)
    title = models.CharField(max_length = 300)
    text = models.TextField()
    #create_time = models.DateTimeField(default = timezone.now)
    published_time = models.DateTimeField(blank = True, null = True)

    def publish(self):
        self.published_time = timezone.now()
        self.save()

    def __str__(self):
        return self.title