from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "slug",
        "author",
        "tags",
        "content",
        "image",
        "published"
    )

    prepopulated_fields = {"slug": ("title",)}

    ordering = ("published", )

admin.site.register(Post, PostAdmin)
