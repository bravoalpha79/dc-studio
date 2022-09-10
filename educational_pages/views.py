from django.shortcuts import render
from .models import Post

def all_posts(request):
    posts = Post.objects.all()
    return render(request, "educational_pages/all_posts.html", {"posts": posts})


def view_post(request, post_slug):
    post = Post.objects.get(slug=post_slug)
    return render(request, "educational_pages/single_post.html", {"post": post})
