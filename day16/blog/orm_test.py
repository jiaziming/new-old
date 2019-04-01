#!/usr/bin/python
# -*-coding:utf-8-*-

import os
os.environ['DJANGO_SETTINGS_MODULE'] ='day16.settings'

import django
django.setup()
from django.db.models import F


from blog import models


#
# entry = models.Entry.objects.get(pk=1)
#
#
# ew_blog= models.Blog.objects.get(id=2)

# obj = models.Entry.objects.get(blog__name__contains='beales')
# #
# # print(obj)

objs = models.Entry.objects.filter(n_comments__lt=F('n_pingbacks'))
print(objs)