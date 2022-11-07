from django.shortcuts import render
from .models import Cooperation

# Create your views here.
def cooperation(request):
    cooperation = Cooperation.objects.all().order_by("-updated_at").first()

    return render(request, "cooperation/cooperation.html", {"cooperation": cooperation})