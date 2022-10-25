from django import template
from django.core.paginator import Paginator

from ..models import *

register = template.Library()


@register.simple_tag()
def get_genres():
    return Genre.objects.all()


@register.simple_tag()
def get_authors():
    return Author.objects.all()

