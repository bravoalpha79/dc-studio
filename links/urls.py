from django.urls import path
from . import views

urlpatterns = [
    path("korisni_linkovi/", views.links, name="links"),
    path("iz_medija/", views.media_links, name="media_links"),
]