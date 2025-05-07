from redpillmusicapp.models import FeaturedSongs,Genra
from redpillmusicapp.MESSAGES.ResponseMessages import ResponseMessage
from redpillmusicapp.MESSAGES.Names import Names
from redpillmusicapp.MESSAGES.ResponseCode import ResponseCode
from redpillmusicapp.UTILITY.ResponseBack import ResponseBack
from .songcontrollers import SongController

songcontroller = SongController()
class FeaturedSongController():

    #get featured song
    def get_featured_song(self):
        try:
            #get data from request
            feat_songs = FeaturedSongs.objects.all()
            print("getting featured songs")
            song_data = []
            for song in feat_songs:
                print('getting song')
                songresp = songcontroller.get_songs(song.song)
                # print(song)
                data = {
                    Names.STATUS:songresp.code,
                    Names.DATA:songresp.data
                }
                song_data.append(data)

            # print(song_data)
            return ResponseBack(code=ResponseCode.SUCCESS, message=ResponseMessage.SONG_FOUND_SUCCESS, data=song_data,local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.SONG_FOUND_ERROR, data=str(e),local=True)
        
        
    #add featured songs
    def add_featured_song(self):
        try:
            # get latest added artist
            genra = Genra.objects.all()
            FeaturedSongs.objects.all().delete()
            for genras in genra:
                songs = genras.genra_songs.all()[:10]
                for song in songs:
                    FeaturedSongs.create(song=song)
            return ResponseBack(code=ResponseCode.SUCCESS, message=ResponseMessage.FEATURED_SONG_ADDED_SUCCESS, data=[],local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.FEATURED_SONG_ADDED_ERROR, data=[],local=True)