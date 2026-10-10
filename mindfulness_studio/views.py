from django.shortcuts import render, redirect
from .models import MindfulnessStudio


def mindfulness_studio(request):
    content = MindfulnessStudio.objects.visible().first()
    if content is None:
        return redirect('home')

    return render(
        request,
        "mindfulness_studio/mindfulness_studio.html",
        {"mindfulness_studio": content}
    )
