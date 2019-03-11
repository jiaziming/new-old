from django.contrib import admin

# Register your models here.

from App01 import models

admin.site.register(models.Author)
admin.site.register(models.Publisher)
admin.site.register(models.Book)