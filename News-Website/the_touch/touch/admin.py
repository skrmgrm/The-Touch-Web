from datetime import date
from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'publish', 'status', 'author', 'graphics']
    list_filter = ['status', 'created',
                   'publish', 'user', 'author', 'graphics']
    search_fields = ['title', 'body']
    raw_id_fields = ('user',)
    date_hierarchy = 'publish'
    ordering = ('status', 'publish')


admin.site.register(Post, PostAdmin)
