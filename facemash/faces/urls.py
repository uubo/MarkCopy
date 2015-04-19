from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^compare$', views.compare, name='compare'),
]