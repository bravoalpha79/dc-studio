from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

class PostAdmin(SummernoteModelAdmin):
    summernote_fields = "content"

    list_display = (
        "title",
        "author",
        "tags",
        "date_published"
    )

    prepopulated_fields = {"slug": ("title",)}

    ordering = ("-date_published", )

admin.site.register(Post, PostAdmin)
