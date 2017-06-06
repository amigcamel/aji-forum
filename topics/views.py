"""Views."""
from datetime import datetime
import uuid

from django.shortcuts import render, HttpResponseRedirect, HttpResponse
from django.conf import settings
from django.core.urlresolvers import reverse

from .forms import TopicForm


def index(request):
    """Index page."""
    topics = sorted(
        settings.TOPICS.items(), key=lambda x: x[1]['upvotes'],
        reverse=True,
    )
    topics = (
        topics
        if request.GET.get('all', '') == 'true'
        else topics[:20]
    )
    return render(request, 'index.html', {'topics': topics})


def vote(request, uuid, target):
    """Vote up/down to a topic."""
    topic = settings.TOPICS.get(uuid)
    if topic:
        topic[target] += 1
    return HttpResponseRedirect(reverse('index'))


def publish(request):
    """Publish a topic."""
    if request.method == 'POST':
        form = TopicForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data['title']
            content = form.cleaned_data['content']
            settings.TOPICS[str(uuid.uuid4())] = {
                'title': title,
                'content': content,
                'datetime': datetime.now(),
                'upvotes': 0,
                'downvotes': 0,
            }
            return HttpResponseRedirect(reverse('index'))
    else:
        form = TopicForm()
    return render(request, 'publish.html', {'form': form})
