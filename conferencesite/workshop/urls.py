from django.conf.urls import url
from workshop import views

urlpatterns = [
    url(r'^$', views.workshop, name='workshop'),

]