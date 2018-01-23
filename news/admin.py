from django.contrib import admin
from . models import Editor, Articles , tags

# Register your models here.

class ArticlesAdmin(admin.ModelAdmin):
    filter_horizontal = ('tags',)

    
admin.site.register(Editor)
admin.site.register(Articles)
admin.site.register(tags)