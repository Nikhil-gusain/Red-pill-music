from redpillmusicapp.models import Artist,Genra,FeaturedArtist
from redpillmusicapp.MESSAGES.ResponseMessages import ResponseMessage
from redpillmusicapp.MESSAGES.Names import Names
from redpillmusicapp.MESSAGES.ResponseCode import ResponseCode
from redpillmusicapp.UTILITY.ResponseBack import ResponseBack
from .artistcontroller import ArtistController
artistcontrolller = ArtistController()
import json
class FeaturedArtistController():

    #function to get featured artist
    def get_featured_artists(self):
        try:
            #get data from request
            feat_artists = FeaturedArtist.objects.all()
            artist_data = []
            for artist in feat_artists:
                artistresp = artistcontrolller.get_artists_data(artist.artist)
                data = {
                    Names.STATUS:artistresp.code,
                    Names.DATA:artistresp.data
                }
                artist_data.append(data)
                
            return ResponseBack(code=ResponseCode.SUCCESS, message=ResponseMessage.ARTIST_UPDATED_SUCCESS,data=artist_data,local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.ARTIST_UPDATED_ERROR, data=str(e),local=True)
        
    #function to get featured artist by genra
    def get_featured_artists_by_genra(self,genra_id):
        try:
            #get data from request
            genra = Genra.objects.get(id =genra_id)
            artists = FeaturedArtist.objects.all()
            artist_data = []
            for artist in artists:
                if artist.artist.Genra.id == genra.id:
                    artistresp = artistcontrolller.get_artists_data(artist.artist)
                    data = {Names.STATUS:artistresp.code,Names.DATA:artistresp.data}
                    artist_data.append(data)
            # print(artist_data)
            return ResponseBack(code=ResponseCode.SUCCESS,message=ResponseMessage.FEATURED_ARTIST_FOUND_SUCCESS, data=artist_data,local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.FEATURED_ARTIST_FOUND_ERROR, data=str(e),local=True)
    
    #function to add featured artist
    def add_featured_artist():
        try:
            # get latest added artist
            FeaturedArtist.objects.all().delete()
            for genra in Genra.objects.all():
                artists = genra.genra_artists.all()[:10]
                for artist in artists:
                    FeaturedArtist.create(artist=artist)
            return ResponseBack(code=ResponseCode.SUCCESS, message=ResponseMessage.FEATURED_ARTIST_ADDED_SUCCESS, data=[],local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.FEATURED_ARTIST_ADDED_ERROR, data=str(e),local=True)