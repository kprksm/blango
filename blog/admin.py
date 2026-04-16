from django.contrib import admin
from blog.models import Tag, Post, Comment

# Register your models here.

class CommentAdmin(admin.ModelAdmin):
  list_display = ('creator','content')
  list_filter = ("creator",)


class PostAdmin(admin.ModelAdmin): 
  prepopulated_fields = {"slug": ("title",)}
  list_filter = ("title", "author")
  list_display =("title", "published_at", "slug")
  # exclude = ["slug"]

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment,CommentAdmin)
