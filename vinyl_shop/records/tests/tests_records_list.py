from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse_lazy
from records.models import Record


class RecordsListTestCase(TestCase):
    fixtures = [
        "record_genre.fixture.json",
        "records.fixture.json",
        "record_label.fixture.json"
    ]

    url = reverse_lazy("records:list")

    def test_list_records(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, HTTPStatus.OK)
        records = (
            Record
            .objects
            .order_by("artist")
            .all()
        )
        records_in_context = response.context["records"]
        self.assertQuerysetEqual(records_in_context, records)
