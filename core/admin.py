from django.contrib import admin

from .models import Content, Section, Sheet


class SheetAdmin(admin.ModelAdmin):
    list_display = ("name", "title")
    search_fields = ("name", "title")


class SectionAdmin(admin.ModelAdmin):
    list_display = ("title", "sheet")
    search_fields = ("title",)
    list_filter = ("sheet",)


class ContentAdmin(admin.ModelAdmin):
    list_display = ("title", "section")
    search_fields = ("title",)
    list_filter = ("section",)


admin.site.register(Sheet, SheetAdmin)
admin.site.register(Section, SectionAdmin)
admin.site.register(Content, ContentAdmin)
