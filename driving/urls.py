from django.urls import path
from . import views

urlpatterns = [
    path("individualni/", views.driving_individual, name="driving_individual"),
    path("tecaj_provozi/", views.driving_group, name="driving_group"),
]