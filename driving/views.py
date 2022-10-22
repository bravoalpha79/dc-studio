from django.shortcuts import render
from .models import DrivingIndividual, DrivingGroup

def driving_individual(request):
    content = DrivingIndividual.objects.all().order_by("-updated_at").first()
    return render(request, "driving/driving_individual.html", {"content": content})

def driving_group(request):
    content = DrivingGroup.objects.all().order_by("-updated_at").first()
    return render(request, "driving/driving_group.html", {"content": content})