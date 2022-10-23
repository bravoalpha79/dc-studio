import django.utils
from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import About

class AboutAdmin(SummernoteModelAdmin):
    summernote_fields = "content"

    list_display = (
        "updated_at",
    )

    ordering = ("-updated_at", )

    def save_model(self, request, obj, form, change):
        obj.updated_at = django.utils.timezone.now()
        obj.save()

admin.site.register(About, AboutAdmin)
