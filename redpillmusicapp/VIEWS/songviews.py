from redpillmusicapp.UTILITY.ResponseBack import ResponseBack
from redpillmusicapp.MESSAGES.ResponseMessages import ResponseMessage
from redpillmusicapp.MESSAGES.Names import Names
from redpillmusicapp.MESSAGES.ResponseCode import ResponseCode
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from redpillmusicapp.CONTROLLERS.SONGCONTROLLERS.featuredsongcontroller import FeaturedSongController
from redpillmusicapp.CONTROLLERS.SONGCONTROLLERS.songcontrollers import SongController
featuredsongscontroller = FeaturedSongController
songcontroller = SongController()


# Song views
#get featured song
@api_view(['GET'])
@permission_classes([AllowAny])
def get_featured_song(request):
    try:
        print("getting featured song")
        featureresp = FeaturedSongController.get_featured_song()
        return ResponseBack(code=featureresp.code, message=featureresp.message, data=featureresp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.FEATURED_SONG_FOUND_ERROR, data=[])
#add featured songs
@api_view(['GET'])
@permission_classes([AllowAny])
def add_featured_song(request):
    try:
        featureresp = featuredsongscontroller.add_featured_song()
        return ResponseBack(code=featureresp.code, message=featureresp.message, data=featureresp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.FEATURED_SONG_ADDED_ERROR, data=[])
#function to add song
@api_view(['POST'])
def add_song(request):
    try:
        addsongresp = songcontroller.add_song(request=request)
        return ResponseBack(code=addsongresp.code, message=addsongresp.message, data=addsongresp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.SONG_CREATED_ERROR, data=[])
#function to edit song
@api_view(['POST'])
def edit_song(request,song_id):
    try:
        songeditresp = songcontroller.edit_song(request=request,song_id=song_id)
        return ResponseBack(code=songeditresp.code, message=songeditresp.message, data=songeditresp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.SONG_UPDATED_ERROR, data=[])

#function to get song
@api_view(['GET'])
@permission_classes([AllowAny])
def get_song(request,song_id):
    try:
        songresp = songcontroller.get_song(song_id=song_id)
        return ResponseBack(code=songresp.code, message=songresp.message, data=songresp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.SONG_FOUND_ERROR, data=[])
#function to delete song
@api_view(['GET'])
@permission_classes([AllowAny])
def delete_song(request,song_id):
    try:
        songcontroller.delete_song(song_id=song_id)
        return ResponseBack(code=ResponseCode.SUCCESS, message=ResponseMessage.SONG_DELETED_SUCCESS, data=[])
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.SONG_DELETED_ERROR, data=[])

#function to get song by genra
@api_view(['GET'])
@permission_classes([AllowAny])
def get_songs_by_genra(request,genra_id):
    try:
        songresp = songcontroller.get_songs_by_genra(genra_id=genra_id)
        return ResponseBack(code=songresp.code, message=songresp.message, data=songresp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.SONG_BY_GENRA_FOUND_ERROR, data=str(e))

#function to get song by artist
@api_view(['GET'])
@permission_classes([AllowAny])
def get_songs_by_artist(request,artist_id):
    try:
        songresp = songcontroller.get_songs_by_artist(artist_id=artist_id)
        return ResponseBack(code=songresp.code, message=songresp.message, data=songresp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.SONG_BY_ARTIST_FOUND_ERROR, data=str(e))