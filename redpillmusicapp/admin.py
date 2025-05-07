from django.contrib import admin
from .models import Artist,FeaturedArtist,FeaturedSongs,Genra,Song,CurrentPill,Submission,DefaultImage,ImageType
# Register your models here.
admin.site.register(Artist)
admin.site.register(FeaturedArtist)
admin.site.register(FeaturedSongs)
admin.site.register(Genra)
admin.site.register(Song)
admin.site.register(CurrentPill)
admin.site.register(Submission)
admin.site.register(DefaultImage)
admin.site.register(ImageType)
