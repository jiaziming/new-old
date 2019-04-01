from django.db import models
from django.utils.html import format_html
# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.EmailField()
    def __str__(self):
        return "<%s %s>" %(self.first_name,self.last_name)


class Publisher(models.Model):
    name = models.CharField(max_length=64,unique=True)
    address = models.CharField(max_length=128)
    city = models.CharField(max_length=64)
    state_province = models.CharField(max_length=30,help_text="请正确填写内容",verbose_name="所属省份")
    country = models.CharField(max_length=50)
    website = models.URLField()
    def __str__(self):
        return "<%s>" %(self.name)


class Book(models.Model):
    name = models.CharField(max_length=128)
    authors = models.ManyToManyField(Author)
    publisher = models.ForeignKey(Publisher,on_delete=models.CASCADE,)
    publish_date = models.DateField()
    status_choices = (('published',u'已出版'),
                      ('producing', u'待出版'),
                      ('forbidden',u'下架'),
                     )
    status = models.CharField(choices=status_choices,max_length=64,default='producing')






    def __str__(self):
        return "<%s>" %(self.name)


    def colored_status(self):
        if self.status == 'published':
            format_td = format_html('<span style="padding: 2px;background-color: yellowgreen;color: white">已出版</span>')

        elif self.status == 'producing':
            format_td = format_html('<span style="padding: 2px;background-color: pink;color: white">待出版</span>')

        elif self.status == 'forbidden':
            format_td = format_html('<span style="padding: 2px;background-color: orange;color: white">下架</span>')

        return format_td

