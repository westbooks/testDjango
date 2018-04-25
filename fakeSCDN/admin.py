from django.contrib import admin
from fakeSCDN.models import BlogsPost
from . import models

# Register your models here.

class BlogsPostAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'create_time']


admin.site.register(BlogsPost, BlogsPostAdmin)

admin.site.register(models.User)
