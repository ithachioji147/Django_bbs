from django import template
from django.utils import timezone
from django.utils.timezone import localtime

register = template.Library()


@register.simple_tag
def get_timezone_class():
    now = localtime(timezone.now())
    if now.hour >= 6 and now.hour < 11:
        return 'morning'
    elif now.hour >= 11 and now.hour < 16:
        return 'noon'
    elif now.hour >= 16 and now.hour < 19:
        return 'afternoon'
    else:
        return 'night'
