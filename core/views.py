from django.views.generic import ListView, TemplateView

from core.models import Sheet


class SheetTemplateView(TemplateView):
    template_name = "sheet.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pk = kwargs.get("pk")
        obj = Sheet.objects.get(id=pk)
        context["obj"] = obj
        return context


class CheatSheetListView(ListView):
    model = Sheet
    template_name = "cheatsheet_list.html"
