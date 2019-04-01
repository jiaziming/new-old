from django.contrib import admin

# Register your models here.

from App01 import models

def make_forbidden(ModelAdmin,request,queryset):
    print('------>:',request,queryset)

    queryset.update(status='forbidden')

    make_forbidden.short_description = 'Set fo forbidden'



class BookAdmin(admin.ModelAdmin):
    list_display = ('id','name','publisher','publish_date','colored_status')
    search_fields = ('name','publisher__name')
    list_filter = ('publisher','publish_date')
    list_editable = ('name','publish_date')
    list_per_page = 10
    make_forbidden
    filter_horizontal = ('authors',)    #for m 2 m
    raw_id_fields = ('publisher',)      #for fk

    actions = [make_forbidden]


admin.site.register(models.Author)
admin.site.register(models.Publisher)
admin.site.register(models.Book,BookAdmin)

