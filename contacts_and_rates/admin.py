import django.utils
from django.contrib import admin

from django_summernote.admin import SummernoteModelAdmin
from .models import ContactInfo, RateList, RateLink


class ContactInfoAdmin(SummernoteModelAdmin):
    summernote_fields = "content"

    list_display = (
        "updated_at",
    )

    ordering = ("-updated_at", )

    def save_model(self, request, obj, form, change):
        obj.updated_at = django.utils.timezone.now()
        obj.save()


class RateListAdmin(admin.ModelAdmin):
    list_display = (
        "updated_at", "ratelist_pdf"
    )

    ordering = ("-updated_at", )

    def save_model(self, request, obj, form, change):
        obj.updated_at = django.utils.timezone.now()
        obj.save()


class RateLinkAdmin(admin.ModelAdmin):
    list_display = (
        "last_updated_at", "ratelink_url" 
    )

    def save_model(self, request, obj, form, change):
        obj.last_updated_at = django.utils.timezone.now()
        obj.save()

    def has_add_permission(self, request):
        return not RateLink.objects.exists()


admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(RateList, RateListAdmin)
admin.site.register(RateLink, RateLinkAdmin)
