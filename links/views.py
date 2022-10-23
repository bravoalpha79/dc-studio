from django.shortcuts import render
from .models import Link, StudentLink, MediaLink

def links(request):
    links = Link.objects.filter(display=True)
    student_links = StudentLink.objects.filter(display=True)
    context = {
        "links": links,
        "student_links": student_links
    }

    return render(request, "links/links.html", context)

def media_links(request):
    links = MediaLink.objects.all()

    return render(request, "links/media_links.html", {"links": links})