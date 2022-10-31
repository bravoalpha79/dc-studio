from django.shortcuts import render
from django.core.paginator import Paginator

from .models import Post

def all_posts(request):
    posts = Post.objects.all().order_by("position")
    
    paginator = Paginator(posts, 5)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    return render(request, "educational_pages/all_posts.html", {"page_obj": page_obj})

def view_post(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    return render(request, "educational_pages/single_post.html", {"post": post})
