from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import TeamMember, Associate

# Apply summernote to all TextField in model.
class TeamMemberAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = "biography"

    list_display = (
        "position", "name_and_title",
    )

    ordering = ("position", )

class AssociateAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = "biography"

    list_display = (
        "position", "name_and_title",
    )

    ordering = ("position", )

admin.site.register(TeamMember, TeamMemberAdmin)
admin.site.register(Associate, AssociateAdmin)
