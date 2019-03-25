from django.contrib import admin

# Register your models here.

from App01 import models

class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','publisher','publish_date')
    search_fields = ('name','publisher__name')
    list_filter = ('publisher','publish_date')
    list_editable = ('name','publish_date')
    list_per_page = 10

    filter_horizontal = ('authors',)    #for m 2 m
    raw_id_fields = ('publisher',)      #for fk


admin.site.register(models.Author)
admin.site.register(models.Publisher)
admin.site.register(models.Book,BookAdmin)

