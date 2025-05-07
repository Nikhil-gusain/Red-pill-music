from django.db import models
from django.contrib.auth.models import User
# Create your models here.

# genra
class Genra(models.Model):
	genra_name = models.CharField(max_length=50)

	def __str__(self):
		return self.genra_name

# artist
class Artist(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	artist_name = models.CharField(max_length=100)
	artist_contact = models.CharField(max_length=100, blank=True)
	profile_pic = models.ImageField(upload_to='artist/profile_pics')
	description = models.TextField()
	No_of_songs = models.IntegerField(default=0)
	Genra = models.ForeignKey(Genra,related_name='genra_artists',on_delete=models.CASCADE)
	Links = models.TextField()
	Creation_date = models.DateTimeField(auto_now_add=True)
	def __str__(self):
		return self.artist_name

# songs model
class Song(models.Model):
	mp3_file = models.FileField(upload_to='songs', blank=True,null=True)
	embeded_link = models.TextField()
	Song_name = models.CharField(max_length=100)
	Genra = models.ForeignKey('Genra', on_delete=models.CASCADE,related_name='genra_songs')
	Artist = models.ForeignKey(Artist, on_delete=models.CASCADE,related_name='artist_songs')
	Lyrics = models.FileField(upload_to='lyrics', blank=True,null=True)

	def __str__(self):
		return self.Song_name

# featured artist
class FeaturedArtist(models.Model):
	artist = models.ForeignKey(Artist, on_delete=models.CASCADE,related_name='featured_artist')
	def __str__(self):
		return f'featured {self.artist.artist_name}'

# featured songs
class FeaturedSongs(models.Model):
	song = models.ForeignKey(Song, on_delete=models.CASCADE)
	def __str__(self):
		return f'featured {self.song.Song_name}'
	
class Submission(models.Model):
	lyrics = models.FileField(upload_to='submissions/lyrics', blank=True)
	music = models.FileField(upload_to='submissions/music', blank=True)
	date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return f'submission on {self.date.date()}'

class CurrentPill(models.Model):
	song = models.ForeignKey(Song, on_delete=models.CASCADE)
	def __str__(self):
		return f'Red pill {self.song.Song_name}'
class CurrentRedPillArtist(models.Model):
	artist = models.ForeignKey(Artist,on_delete=models.CASCADE)

	def __str__(self):
		return f'Red pill artist {self.artist.artist_name}'

class ImageType(models.Model):
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name

class DefaultImage(models.Model):
	type = models.ForeignKey(ImageType, on_delete=models.CASCADE)
	image = models.FileField(upload_to='default_images')

	def __str__(self):
		return f'{self.type.name} default image'
	

#last updated model
class LastUpdated(models.Model):
	featuredartist = models.DateField()
	featuredsong = models.DateField()

	def __str__(self):
		return f'last updated on {self.featuredartist}'
