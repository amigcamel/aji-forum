"""Views."""
from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse


def index(request):
    """Index page."""
    topics = sorted(
        settings.TOPICS.items(), key=lambda x: x[1]['upvotes'],
        reverse=True,
    )
    return render(request, 'index.html', {'topics': topics})


def vote(request, uuid, target):
    """Vote up/down to a topic."""
    topic = settings.TOPICS.get(uuid)
    if topic:
        topic[target] += 1
    return HttpResponseRedirect(reverse('index'))
