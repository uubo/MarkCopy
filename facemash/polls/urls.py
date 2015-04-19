from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^hui$', views.index, name='index'),
]