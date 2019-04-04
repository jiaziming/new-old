from django.contrib import admin

# Register your models here.

from blog import models



class EntryAdmin(admin.ModelAdmin):
    list_display = ('blog','headline','pub_date','mod_date','n_comments',
                    'n_pingbacks',)




admin.site.register(models.Blog)
admin.site.register(models.Entry,EntryAdmin)
admin.site.register(models.Author)
