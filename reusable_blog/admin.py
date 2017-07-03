# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Post    # . denotes import from same directory as this file (e.g blog_app)

admin.site.register(Post)
