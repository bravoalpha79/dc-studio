from django.shortcuts import render
from django.contrib.postgres.search import SearchVector

from educational_pages.models import Post
from links.models import MediaLink


def index(request):
    """ A view to return the index page """

    return render(request, "home/index.html")

def search(request):
    q = request.GET["query"] if "query" in request.GET else None
    posts = None
    links = None

    if q:
        posts = Post.objects.annotate(search=SearchVector("title", "content")).filter(search=q)
        links = MediaLink.objects.annotate(search=SearchVector("title", "summary")).filter(search=q)
    
    context = {
        "query": q,
        "posts": posts,
        "links": links
    }

    return render(request, "home/search.html", context)
