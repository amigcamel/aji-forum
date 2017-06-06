"""Forms."""
from django import forms


class TopicForm(forms.Form):
    """Form for a topic."""

    title = forms.CharField(label='Title', max_length=100)
    content = forms.CharField(label='Content', max_length=255)
