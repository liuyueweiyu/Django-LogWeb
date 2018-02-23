from django.contrib import admin
from .models import Log


# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title']
    class Media:
        js = ('/static/kindeditor-4.1.11/kindeditor-all-min.js',
              '/static/kindeditor-4.1.11/lang/zh-CN.js',
              '/static/kindeditor-4.1.11/config.js')

admin.site.register(Log,ArticleAdmin)