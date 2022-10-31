from itertools import chain
from django.shortcuts import render
from django.core.paginator import Paginator
from django.contrib.postgres.search import SearchVector

from educational_pages.models import Post
from links.models import MediaLink


def index(request):
    """ A view to return the index page """

    return render(request, "home/index.html")

def search(request):
    q = request.GET["query"] if "query" in request.GET else None
    results = None

    if q:
        posts = Post.objects.annotate(search=SearchVector("title", "content")).filter(search=q)
        links = MediaLink.objects.annotate(search=SearchVector("title", "summary")).filter(search=q)
        results = list(chain(posts, links))

        paginator = Paginator(results, 5)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)

    
    context = {
        "query": q,
        "results": results,
        "page_obj": page_obj 
    }

    return render(request, "home/search.html", context)
