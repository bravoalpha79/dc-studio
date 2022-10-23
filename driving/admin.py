import django.utils
from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import DrivingIndividual, DrivingGroup

class DrivingIndividualAdmin(SummernoteModelAdmin):
    summernote_fields = "content"

    list_display = (
        "updated_at",
    )

    ordering = ("-updated_at", )

    def save_model(self, request, obj, form, change):
        obj.updated_at = django.utils.timezone.now()
        obj.save()


class DrivingGroupAdmin(SummernoteModelAdmin):
    summernote_fields = "content"

    list_display = (
        "updated_at",
    )

    ordering = ("-updated_at", )

    def save_model(self, request, obj, form, change):
        obj.updated_at = django.utils.timezone.now()
        obj.save()

admin.site.register(DrivingIndividual, DrivingIndividualAdmin)
admin.site.register(DrivingGroup, DrivingGroupAdmin)
