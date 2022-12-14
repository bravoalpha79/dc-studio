from django.shortcuts import render
from .models import Associate, TeamMember

# Create your views here.
def view_team(request):
    team_members = TeamMember.objects.all().order_by("position")
    associates = Associate.objects.all().order_by("position")
    context = {
        "team_members": team_members,
        "associates": associates
    }
    return render(request, "team/team.html", context)
