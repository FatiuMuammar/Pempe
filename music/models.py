from django.db import models
from django.core.urlresolvers import reverse


class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    # This will show after i create an album
    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk': self.pk})

    # this is how i represent our Album in html template
    def __str__(self):
        return self.album_title + " - " + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    # this is how i represent my Song in html template
    def __str__(self):
        return self.song_title
