from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView

from .models import Record


class RecordListView(ListView):
    template_name = "records/record_list.html"
    queryset = (
        Record
        .objects
        .order_by("artist")
        .all()
    )
    context_object_name = "records"


class RecordDetailView(DetailView):
    template_name = "records/record_details.html"
    queryset = (
        Record
        .objects
        .select_related("record_label")
        .prefetch_related("genre")
    )


class RecordDeleteView(DeleteView):
    template_name = "records/record_delete.html"
    model = Record
    success_url = reverse_lazy("records:list")
