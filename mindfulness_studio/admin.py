import django.utils
from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import MindfulnessStudio


class MindfulnessStudioAdmin(SummernoteModelAdmin):
    summernote_fields = "content"

    list_display = (
        "updated_at", "is_published"
    )

    ordering = ("-updated_at", )

    def save_model(self, request, obj, form, change):
        obj.updated_at = django.utils.timezone.now()
        obj.save()

    def has_add_permission(self, request):
        return not MindfulnessStudio.objects.exists()


admin.site.register(MindfulnessStudio, MindfulnessStudioAdmin)
