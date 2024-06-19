import random

from django import template

register = template.Library()


BOOTSTRAP_COLOR_CLASSES = [
    "text-bg-primary",
    "text-bg-secondary",
    "text-bg-success",
    "text-bg-danger",
    "text-bg-warning",
    "text-bg-info",
    "text-bg-light",
    "text-bg-dark",
]


@register.simple_tag
def random_bootstrap_color():
    return random.choice(BOOTSTRAP_COLOR_CLASSES)
