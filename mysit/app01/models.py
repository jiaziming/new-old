from django.db import models

# Create your models here.

class userinfo(models.Model):

    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
    age = models.IntegerField()

# obj = userinfo()
# [obj1,obj2,obj3]