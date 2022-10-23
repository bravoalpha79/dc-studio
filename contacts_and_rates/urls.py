from django.urls import path
from . import views

urlpatterns = [
    path("kontakti_i_informacije/", views.contacts, name="contacts"),
    path("cjenik/", views.rates, name="rates"),
]