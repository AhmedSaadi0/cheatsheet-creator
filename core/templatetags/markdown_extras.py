from django import template
from markdown2 import markdown

register = template.Library()


@register.filter(name="markdown_to_html")
def markdown_to_html(markdown_text):
    return markdown(markdown_text, extras=["fenced-code-blocks"])
