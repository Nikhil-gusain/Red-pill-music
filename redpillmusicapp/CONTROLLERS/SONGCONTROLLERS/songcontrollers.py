from redpillmusicapp.models import Song,Genra,Artist
from redpillmusicapp.MESSAGES.ResponseMessages import ResponseMessage
from redpillmusicapp.MESSAGES.Names import Names
from redpillmusicapp.MESSAGES.ResponseCode import ResponseCode
from redpillmusicapp.UTILITY.ResponseBack import ResponseBack
from redpillmusicapp.UTILITY.helperfunctions import is_youtube_video_link 

class SongController():
    #function to get all songs
    def get_all_songs(self):
        try:
            songs = Song.objects.all()
            song_data = []
            for song in songs:
                songresp = self.get_songs(song)
                data = {Names.STATUS:songresp.code,Names.DATA:songresp.data}
                song_data.append(data)
            return ResponseBack(code=ResponseCode.SUCCESS, message=ResponseMessage.ALL_SONGS_FOUND_SUCCESS, data=song_data,local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.ALL_SONGS_FOUND_ERROR, data=str(e),local=True)

    #function to get song data
    def get_songs(self,song):
        try:
            song_data = {
                Names.SONG_ID:song.id,
                Names.SONG_NAME:song.Song_name,
                Names.SONG_GENRA:song.Genra.genra_name,
                Names.EMBED_LINK:song.embeded_link
            }
            return ResponseBack(code=ResponseCode.SUCCESS, message=ResponseMessage.SONG_DATA_FOUND_SUCCESS, data=song_data,local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.SONG_DATA_FOUND_ERROR, data=str(e),local=True)

    #function to add song
    def add_song(self,request):
        try:
            #get data from request
            song_name = request.data.get(Names.SONG_NAME, Names.UNTITLED)
            embeded_link = request.data.get(Names.EMBED_LINK)

            if not is_youtube_video_link(embeded_link):
                return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.SONG_EMBEDED_LINK_ERROR, data=[])

            genra_id = request.data.get(Names.GENRA_ID)
            genra = Genra.objects.get(id=genra_id)

            artist_id = request.data.get(Names.ARTIST_ID)


            artist = Artist.objects.get(id =artist_id)
            Song.objects.create(song_name=song_name,genra=genra,artist=artist,embeded_link=embeded_link)
            return ResponseBack(code=ResponseCode.SUCCESS, message=ResponseMessage.SONG_CREATED_SUCCESS, data=[],local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.SONG_CREATED_ERROR, data=[],local=True)
    #function to edit song
    def edit_song(self,request,song_id):
        try:
            #get data from request
            song = Song.objects.filter(id=song_id).first()
            if not song:
                return ResponseBack(code=ResponseCode.ERROR, message="Song not found", data=[])

            song.song_name = request.data.get(Names.SONG_NAME, song.song_name)
            song.embeded_link = request.data.get(Names.EMBED_LINK, song.embeded_link)
            song.save()
            return ResponseBack(code=ResponseCode.SUCCESS, message=ResponseMessage.SONG_UPDATED_SUCCESS, data=[],local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.SONG_UPDATED_ERROR, data=[],local=True)
    
    #function to get song
    def get_song(self,song_id):
        try:
            #get data from request
            song = Song.objects.get(id =song_id)
            songresp = self.get_songs(song)
            
            return ResponseBack(code=songresp.code, message=songresp.message, data=songresp.data,local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.SONG_FOUND_ERROR, data=[],local=True)
    #function to delete song
    def delete_song(self,song_id):
        try:
            #get data from request
            song = Song.objects.filter(id =song_id).first()
            song.delete()
            return ResponseBack(code=ResponseCode.SUCCESS, message=ResponseMessage.SONG_DELETED_SUCCESS, data=[],local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.SONG_DELETED_ERROR, data=[],local=True)
    
    # function to get songs by genra
    def get_songs_by_genra(self,genra_id):
        try:
            #get data from request
            genra = Genra.objects.filter(id =genra_id).first()
            songs = genra.genra_songs.all()
            song_data = []
            for song in songs:
                songresp = self.get_songs(song)
                data = {Names.STATUS:songresp.code,Names.DATA:songresp.data}
                song_data.append(data)
            return ResponseBack(code=ResponseCode.SUCCESS, message=ResponseMessage.SONG_BY_GENRA_FOUND_SUCCESS, data=song_data,local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.SONG_BY_GENRA_FOUND_ERROR, data=str(e),local=True)
        
    #function to get song by artist
    def get_songs_by_artist(self,artist_id):
        try:
            #get data from request
            artist = Artist.objects.filter(id =artist_id).first()
            songs = artist.artist_songs.all()
            song_data = []
            for song in songs:
                songresp = self.get_songs(song)
                data = {Names.STATUS:songresp.code,Names.DATA:songresp.data}
                song_data.append(data)
            return ResponseBack(code=ResponseCode.SUCCESS, message=ResponseMessage.SONG_BY_ARTIST_FOUND_SUCCESS, data=song_data,local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.SONG_BY_ARTIST_FOUND_ERROR, data=str(e),local=True)