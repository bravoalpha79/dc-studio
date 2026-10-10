import django.utils
from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import ExpertEducation


class ExpertEducationAdmin(SummernoteModelAdmin):
    summernote_fields = "content"

    list_display = (
        "position", "title", "updated_at", "is_published"
    )

    prepopulated_fields = {"slug": ("title",)}

    ordering = ("position", )

    def save_model(self, request, obj, form, change):
        obj.updated_at = django.utils.timezone.now()
        obj.save()


admin.site.register(ExpertEducation, ExpertEducationAdmin)
