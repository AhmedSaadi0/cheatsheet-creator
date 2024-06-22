from django.urls import path

from core.views import CheatSheetListView, SheetTemplateView

urlpatterns = [
    path(
        route="sheet/<pk>",
        view=SheetTemplateView.as_view(),
        name="sheet_template_view",
    ),
    path(
        route="",
        view=CheatSheetListView.as_view(),
        name="cheat_sheet_list_view",
    ),
]
