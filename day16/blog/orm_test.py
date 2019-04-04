#!/usr/bin/python
# -*-coding:utf-8-*-

import os
os.environ['DJANGO_SETTINGS_MODULE'] ='day16.settings'

import django
django.setup()
from django.db.models import F,Q


from blog import models
from django.db.models import Avg,Sum,Min,Count



# print(models.Entry.objects.all().aggregate(Avg('n_pingbacks'),Sum('n_pingbacks'),
#                                            Min('n_pingbacks'),
#                                            ))



from App01 import models as Book_models
#
# pub_obj = Book_models.Publisher.objects.last()
# #print(pub_obj.name,pub_obj.book_set.select_related())      反向关联查询
#
# pub_objs = Book_models.Publisher.objects.annotate(book_nums=Count('book'))
#
#
# for Publisher in pub_objs:                  分离聚合
#     print(Publisher.book_nums)
#



# entry = models.Entry.objects.get(pk=1)
#
#
# ew_blog= models.Blog.objects.get(id=2)

# obj = models.Entry.objects.get(blog__name__contains='beales')
# #
# # print(obj)

#objs = models.Entry.objects.filter(n_comments__lt=F('n_pingbacks'))

#objs = models.Entry.objects.filter(n__comments__lte=F('n_pingbacks')/2)
#select n_comments,n_pingbacks from Entry where n_comments <n_pingbacks

#objs = models.Entry.objects.filter(rating__lt=F('n_comments') + F('n_pingbacks'))


#select n_comments,n_pingbacks ,rating from blog_entry where rating >(n_comments + n_pingbacks)

# objs =models.Entry.objects.filter(n_comments__lte=F('n_comments'),
#                                   pub_date__gt='2016-05-20')

# objs = models.Entry.objects.filter(Q(n_comments__lte=F('n_pingbacks')) | Q(pub_date__lt='2016-05-14'))
# print(objs)
#
#
# for obj in objs:
#
#     print(obj)
#

#print(objs)

print(Book_models.Book.objects.values_list('publish_date').annotate(Count('publish_date')))   #查询次数