from django.contrib import admin

from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import About

class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = "content"

    list_display = (
        "content",
        "created_at"
    )

    ordering = ("-created_at", )

admin.site.register(About, AboutAdmin)
