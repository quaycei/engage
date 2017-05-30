from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User


class Tag(models.Model):
    name = models.CharField(max_length=50)
    related_tag = models.ManyToManyField('self', blank=True, default=None)

    def __str__(self):
        return self.name 


class Tool(models.Model):
    creator = models.ForeignKey(User, default=None, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False, null=True)
    tags = models.ManyToManyField('Tag', default=None, blank=True)
    icon_url = models.CharField(max_length=140, default=None, blank=True, null=True)
    video_url = models.CharField(max_length=140, default=None, blank=True, null=True)
    name = models.CharField(max_length=50)
    link = models.CharField(max_length=140, default=None, blank=True, null=True)
    tagline = models.CharField(max_length=140, default=None, blank=True, null=True)
    description = models.TextField(max_length=300, null=True, default=None, blank=True)


    def __str__(self):
        return self.name 
