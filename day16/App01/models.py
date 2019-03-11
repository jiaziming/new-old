from django.db import models

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
    def __str__(self):
        return "<%s>" %(self.name)