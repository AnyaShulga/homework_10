from django.urls import path

from .views import (RecordListView,
                    RecordDeleteView,
                    RecordDetailView
                    )

app_name = "records"

urlpatterns = [
    path("", RecordListView.as_view(), name="list"),
    path("<int:pk>", RecordDetailView.as_view(), name="details"),
    path("<int:pk>/confirm-delete", RecordDeleteView.as_view(), name="delete"),
]