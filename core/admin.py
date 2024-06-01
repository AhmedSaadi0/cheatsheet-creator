from django.contrib import admin

from .models import Description, Sheet, Title


class SheetAdmin(admin.ModelAdmin):
    list_display = ("name", "sheet_title")
    search_fields = ("name", "sheet_title")


class TitleAdmin(admin.ModelAdmin):
    list_display = ("title", "sheet")
    search_fields = ("title",)
    list_filter = ("sheet",)


class DescriptionAdmin(admin.ModelAdmin):
    list_display = ("description", "sheet_title")
    search_fields = ("description",)
    list_filter = ("sheet_title",)


admin.site.register(Sheet, SheetAdmin)
admin.site.register(Title, TitleAdmin)
admin.site.register(Description, DescriptionAdmin)
