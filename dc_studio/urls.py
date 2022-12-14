"""dc_studio URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('home.urls')),
    path('psihoedukativni_kutak/', include('educational_pages.urls')),
    path('strucni_tim/', include('team.urls')),
    path('o_klinickom_studiju/', include('about.urls')),
    path('linkovi/', include('links.urls')),
    path('strah_od_voznje/', include('driving.urls')),
    path('info/', include('contacts_and_rates.urls')),
    path('pravne_osobe/', include('cooperation.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
