from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse_lazy

from records.models import RecordLabel, RecordGenre, Record


class RecordsDetailsTestCase(TestCase):
    def setUp(self):
        self.rec_label = RecordLabel.objects.create(name="Label")
        self.rec_genre = RecordGenre.objects.create(genre="genre")
        self.record = Record.objects.create(
            artist="Artist",
            album="Album",
            year=1989,
            condition="NM",
            record_label=self.rec_label
        )

    def tearDown(self):
        del self.record

    def test_details_records(self):
        self.record.genre.add(self.rec_genre)
        url = reverse_lazy("records:details", args=[self.record.pk])

        response = self.client.get(url)

        record_in_context = response.context["record"]

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(record_in_context, self.record)
