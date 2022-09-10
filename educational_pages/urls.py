from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_posts, name="all_posts"),
    path("<post_slug>/", views.view_post, name="view_post"),
]