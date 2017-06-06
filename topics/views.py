"""Views."""
from copy import deepcopy

from django.shortcuts import render
from django.conf import settings
# from django.core.urlresolvers import reverse


def index(request):
    """Index page."""
    return render(request, 'index.html', {'topics': settings.TOPICS})
    TOPIC = {
        'title': '',
        'content': '',
        'upvotes': 0,
        'downvotes': 0,
    }
    settings.TOPICS.append(deepcopy(settings.TOPIC))
    return HttpResponse(settings.TOPICS)
