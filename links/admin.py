from django.contrib import admin

from .models import Link, StudentLink, MediaLink


class LinkAdmin(admin.ModelAdmin):
    list_display = (
        "url", "title", "display"
    )

    ordering = ("display", )


class StudentLinkAdmin(admin.ModelAdmin):
    list_display = (
        "url", "title", "display"
    )

    ordering = ("display", )

class MediaLinkAdmin(admin.ModelAdmin):
    list_display = (
        "url", "title", "display"
    )

    ordering = ("display", )

admin.site.register(Link, LinkAdmin)
admin.site.register(StudentLink, StudentLinkAdmin)
admin.site.register(MediaLink, MediaLinkAdmin)
