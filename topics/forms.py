"""Forms."""
from django import forms


class TopicForm(forms.Form):
    """Form for a topic."""

    title = forms.CharField(label='title', max_length=100)
    content = forms.CharField(label='content', max_length=255)
