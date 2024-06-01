from django.db import models

# Create your models here.
from django.utils.translation import gettext_lazy as _


class Sheet(models.Model):
    name = models.CharField(
        max_length=200,
        verbose_name=_("Name"),
    )

    sheet_title = models.CharField(
        max_length=200,
        verbose_name=_("Title"),
    )

    def __str__(self):
        return self.name


class Title(models.Model):
    title = models.CharField(
        max_length=200,
        verbose_name=_("Title"),
    )

    sheet = models.ForeignKey(
        to="Sheet",
        on_delete=models.CASCADE,
        verbose_name=_("Sheet"),
    )

    def __str__(self):
        return self.title


class Description(models.Model):
    description = models.TextField()

    sheet_title = models.ForeignKey(
        to="Title",
        on_delete=models.CASCADE,
        verbose_name=_("Title"),
        related_name="description_sheet_title",
    )

    def __str__(self):
        return self.description
