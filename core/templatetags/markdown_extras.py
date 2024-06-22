import markdown
from django import template

register = template.Library()


@register.filter(name="markdown_to_html")
def markdown_to_html(markdown_text):
    if not isinstance(markdown_text, str):
        return markdown_text

    try:
        html = markdown.markdown(
            markdown_text,
            extensions=[
                "markdown.extensions.fenced_code",
                "markdown.extensions.tables",
                "markdown.extensions.footnotes",
                "markdown.extensions.codehilite",
                "markdown.extensions.meta",
                "markdown.extensions.sane_lists",
                "markdown.extensions.toc",
            ],
            output_format="html5",
        )
    except Exception as e:
        return f"Error processing markdown: {e}"

    return html
