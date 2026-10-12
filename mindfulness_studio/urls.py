from django.urls import path
from . import views

urlpatterns = [
    path("", views.mindfulness_studio, name="mindfulness_studio"),
]