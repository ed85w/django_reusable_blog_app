# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.utils import timezone
from django.conf import settings

class Post(models.Model):
    # author is linked to a registered user in the 'auth_user' table
    # author = models.ForeignKey('auth.User')

    author = models.ForeignKey(settings.AUTH_USER_MODEL)    # changed from the line above to allow decoupling/reusing
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)  # Record how often a post is seen
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    # identify blog entries on admin page - title used as identifier
    def __unicode__(self):
        return self.title