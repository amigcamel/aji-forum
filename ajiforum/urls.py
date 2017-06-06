"""URL Configuration."""
from django.conf.urls import url
import topics.views

urlpatterns = [
    url(r'^$', topics.views.index, name='index'),
    url(
        r'(?P<uuid>[a-zA-Z0-9-]{36})/(?P<target>(upvotes|downvotes))$',
        topics.views.vote,
        name='vote'
    ),
]
