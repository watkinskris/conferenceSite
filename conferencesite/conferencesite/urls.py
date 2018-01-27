"""conferencesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from conferencesite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$|^index/$|^homepage/$|^home/$', views.index, name='index'),
    url(r'^activities/$|^funstufftodo/$', views.activities, name='activities'),
    url(r'^meals/', views.meals, name='meals'),
    url(r'^keynote/', views.keynote, name='keynote'),
    url(r'^workshops?[a-zA-Z]*/', include('workshop.urls')),
    url(r'^registration/', include('registrant.urls')),
    url(r'^thankyou/', include('registrant.urls')),
    url(r'^awards?/', include('awardnominee.urls')),
    url(r'^nominees?/', include('awardnominee.urls')),
    url(r'^polls?/', include('awardnominee.urls')),
    url(r'^vote/', include('awardnominee.urls')),
    url(r'^nametags8/$', views.nametag8, name='nametags8'),
    url(r'^nametags10/$', views.nametag10, name='nametags10'),
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
