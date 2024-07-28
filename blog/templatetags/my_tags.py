from django import template

from clients.models import Client
from mailings.models import Mailing

register = template.Library()


@register.filter()
def media_filter(path):
    if path:
        return f"/media/{path}"
    return "#"


@register.simple_tag
def mailings_total():
    return Mailing.objects.count()


@register.simple_tag
def mailings_active():
    return Mailing.objects.filter(status='SENDING').count()


@register.simple_tag
def unique_clients():
    return Client.objects.order_by().values_list('email').distinct().count()
