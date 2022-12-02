from django.db import models


class RecordLabel(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Record(models.Model):
    artist = models.CharField(max_length=30)
    album = models.CharField(max_length=40)
    year = models.IntegerField()
    condition = models.CharField(max_length=3)
    genre = models.ManyToManyField("records.RecordGenre")
    record_label = models.ForeignKey(RecordLabel, on_delete=models.PROTECT)

    def __str__(self):
        return self.album


class RecordGenre(models.Model):
    genre = models.CharField(max_length=20)

    def __str__(self):
        return self.genre
