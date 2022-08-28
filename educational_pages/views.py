from django.shortcuts import render
from .models import Post

def all_posts(request):
    posts = Post.objects.all()
    return render(request, "educational_pages/all_posts.html", {"posts": posts})
