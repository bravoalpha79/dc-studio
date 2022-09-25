from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Post

# Apply summernote to all TextField in model.
class PostAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = "content"

    list_display = (
        "title",
        "author",
        "tags",
        "published"
    )

    prepopulated_fields = {"slug": ("title",)}

    ordering = ("-published", )

admin.site.register(Post, PostAdmin)
