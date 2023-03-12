import datetime

from django.db import models
from django.contrib import admin
from django.utils import timezone

# Create your models here.

class Picture(models.Model):
    picture_text = models.CharField(max_length=500)
    picture = models.ImageField(upload_to='images')
    pub_date = models.DateTimeField('date published')
    comments = models.IntegerField(default=0)

    def __str__(self) -> str:
        return self.picture_text

    @admin.display(
        boolean=True,
        ordering='pub_date',
        description='Published recently?'
    )
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now

class Comment(models.Model):
    picture = models.ForeignKey(Picture, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=500)
    likes = models.IntegerField(default=0)

    def __str__(self):
        return self.comment_text
