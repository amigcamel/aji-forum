"""URL Configuration."""
from django.conf.urls import url
import topics.views

urlpatterns = [
    url(r'^$', topics.views.index, name='index'),
]
