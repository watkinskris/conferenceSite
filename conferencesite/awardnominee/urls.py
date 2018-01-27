from django.conf.urls import url
from awardnominee import views

urlpatterns = [
    url(r'^$', views.awards, name='awards'),

]