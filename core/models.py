from django.db import models
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _


class Sheet(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name=_("Sheet Name"),
        help_text=_("The name of the cheat sheet."),
    )

    title = models.CharField(
        max_length=200,
        verbose_name=_("Sheet Title"),
        help_text=_("The title of the cheat sheet."),
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse_lazy("sheet_template_view", kwargs={"pk": self.pk})

    def get_all_sections(self):
        return self.sections.all()

    class Meta:
        verbose_name = _("Sheet")
        verbose_name_plural = _("Sheets")
        ordering = ["name"]


class Section(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name=_("Section Title"),
        help_text=_("The title of the section."),
    )

    header = models.CharField(
        max_length=200,
        verbose_name=_("Section Header"),
        blank=True,
        help_text=_("An optional header for the section."),
    )

    sheet = models.ForeignKey(
        to="Sheet",
        on_delete=models.CASCADE,
        verbose_name=_("Sheet"),
        related_name="sections",
        help_text=_("The cheat sheet this section belongs to."),
    )

    ordering = models.SmallIntegerField(
        verbose_name=_("Ordering"),
        help_text=_(
            "Set a number to order the placement of this content, lower mean higher"
        ),
        default=0,
    )

    def __str__(self):
        return f"{self.sheet} - {self.title}"

    def get_all_content(self):
        return self.contents.all()

    class Meta:
        verbose_name = _("Section")
        verbose_name_plural = _("Sections")
        ordering = ["ordering"]


class Content(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name=_("Content Title"),
        help_text=_("The title of the content."),
    )

    message = models.TextField(
        verbose_name=_("Content Message"),
        help_text=_("The detailed content message."),
    )

    section = models.ForeignKey(
        to="Section",
        on_delete=models.CASCADE,
        verbose_name=_("Section"),
        related_name="contents",
        help_text=_("The section this content belongs to."),
    )

    ordering = models.SmallIntegerField(
        verbose_name=_("Ordering"),
        help_text=_(
            "Set a number to order the placement of this content, lower mean higher"
        ),
        default=0,
    )

    def __str__(self):
        return f"{self.section} - {self.title}"

    class Meta:
        verbose_name = _("Content")
        verbose_name_plural = _("Contents")
        ordering = ["ordering"]
