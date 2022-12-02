from http import HTTPStatus

from django.test import TestCase, RequestFactory
from django.urls import reverse_lazy
from ..models import Record, RecordLabel, RecordGenre
from records.views import RecordDeleteView


class RecordsDeleteTestCase(TestCase):

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
        self.record.delete()


    def test_delete_records(self):
        self.record.genre.add(self.rec_genre)
        url = reverse_lazy("records:delete", args=[self.record.pk])

        response = self.client.get(url)

        record_in_context = response.context["record"]

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertEqual(record_in_context, self.record)

    def test_record_delete_in_context(self):
        url = reverse_lazy("records:delete", args=[self.record.pk])
        request = RequestFactory().get(url)
        view = RecordDeleteView()
        context = view.setup(request)

        self.assertEqual(None, context)