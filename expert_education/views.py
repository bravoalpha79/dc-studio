from django.shortcuts import render, redirect
from .models import ExpertEducation


def expert_education(request, slug):
    page = ExpertEducation.objects.visible().filter(slug=slug).first()
    if page is None:
        return redirect('home')

    return render(
        request,
        "expert_education/expert_education.html",
        {"education": page}
    )
