from django.contrib import admin
from blog.models import Tag, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin): 
  prepopulated_fields = {"slug": ("title",)}
  list_filter = ("title", "author")
  list_display =("title", "published_at", "slug")
  # exclude = ["slug"]

admin.site.register(Tag)
admin.site.register(Post, PostAdmin)
