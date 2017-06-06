"""Views."""
from copy import deepcopy

from django.shortcuts import HttpResponse
from django.conf import settings
# from django.core.urlresolvers import reverse


def index(request):
    """Index page."""
    settings.TOPICS.append(deepcopy(settings.TOPIC))
    return HttpResponse(settings.TOPICS)
