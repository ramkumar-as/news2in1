# your_app/templatetags/my_filters.py
import re
from django import template

register = template.Library()

@register.filter(name='get')
def get(d, key):
    """Return the value for a given key from a dictionary."""
    return d.get(key, None)

@register.filter
def youtube_id(url):
    if 'youtu.be' in url:
        return url.split('/')[-1]
    if 'youtube.com' in url:
        match = re.search(r"v=([a-zA-Z0-9_-]+)", url)
        if match:
            return match.group(1)
    return None

@register.filter
def camelcase(value):
    
    return value.capitalize()