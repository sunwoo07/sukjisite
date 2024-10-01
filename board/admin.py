from django.contrib import admin

from board.models import Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author')


admin.site.register(Post, PostAdmin)
