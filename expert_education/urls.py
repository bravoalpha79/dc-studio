from django.urls import path
from django.views.generic import RedirectView
from . import views

urlpatterns = [
    path("", RedirectView.as_view(pattern_name="home")),
    path("<slug:slug>/", views.expert_education, name="expert_education")
]
