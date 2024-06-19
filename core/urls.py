from django.urls import path

from core.views import SheetTemplateView

urlpatterns = [
    path(
        route="sheet/<pk>",
        view=SheetTemplateView.as_view(),
        name="sheet_template_view",
    )
]
