from django.db import models
from django.core.urlresolvers import reverse

#every album will have a special id column
class Album(models.Model):
    artist = models.CharField(max_length=250) #columns
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk}) # kwargs = key word args, primary key
    
    def __str__(self): #string representation of an obj
        return self.album_title + ' - ' + self.artist
    
class Song(models.Model):
    #each song is linked to an album
    album = models.ForeignKey(Album, on_delete=models.CASCADE) # key of album; when album is deleted all the songs are deleted as well
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default = False)
    
    def __str__(self):
        return self.song_title