from django.conf.urls import url
from registrant import views

urlpatterns = [
    url(r'^$', views.registration, name='registration'),
]
