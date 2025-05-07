from redpillmusicapp.CONTROLLERS.ARTISTCONTROLLERS.artistcontroller import ArtistController
from redpillmusicapp.CONTROLLERS.ARTISTCONTROLLERS.featuredartistcontroller import FeaturedArtistController
from redpillmusicapp.UTILITY.ResponseBack import ResponseBack
from redpillmusicapp.MESSAGES.ResponseMessages import ResponseMessage
from redpillmusicapp.MESSAGES.Names import Names
from rest_framework.decorators import api_view,permission_classes
from redpillmusicapp.MESSAGES.ResponseCode import ResponseCode
from redpillmusicapp.UTILITY.ResponseBack import ResponseBack
from rest_framework.permissions import AllowAny
artistcontroller  = ArtistController()
featuredartist = FeaturedArtistController()
# Artist views

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_artists(request):
    try:
        artistresp = artistcontroller.get_artists(req_type=Names.API)
        return ResponseBack(code=artistresp.code, message=artistresp.message, data=artistresp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.ARTISTS_FOUND_ERROR, data=str(e))
#create artist
@api_view(['POST'])
def create_artist(request):
    try:
        resp = artistcontroller.create_artist(request=request)

        return ResponseBack(code=resp.code, message=resp.message, data=resp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.ARTIST_CREATED_ERROR, data=str(e))
    
# function to upsate artist
@api_view(['POST'])
def update_artist(request,artist_id):
    try:
        resp = artistcontroller.update_artist(request=request,artist_id=artist_id)

        return ResponseBack(code=resp.code, message=resp.message, data=resp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.ARTIST_UPDATED_ERROR, data=str(e))
# function to get artist
@api_view(['GET'])
@permission_classes([AllowAny])
def get_artist(request,artist_id):
    try:
        resp = artistcontroller.get_artist(artist_id=artist_id,req_type=Names.API)

        return ResponseBack(code=resp.code, message=resp.message, data=resp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.ARTIST_FOUND_ERROR, data=str(e))
#function to delete artist
@api_view(['POST'])
def delete_artist(request,artist_id):
    try:
        resp = artistcontroller.delete_artist(artist_id = artist_id)
        return ResponseBack(code=resp.code, message=resp.message, data=resp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.ARTIST_DELETED_ERROR, data=str(e))

#function to get artist by genra
@api_view(['GET'])
@permission_classes([AllowAny])
def get_artists_by_genra(request,genra_id):
    try:
        resp = artistcontroller.get_artists_by_genra(genra_id=genra_id,req_type=Names.API)
        return ResponseBack(code=resp.code, message=resp.message, data=resp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.ARTIST_FOUND_ERROR, data=str(e))
    
#*********************************** FEATURED ARTIST FUNCTION START HERE ***********************************
#function to get featured artist
@api_view(['GET'])
@permission_classes([AllowAny])
def get_featured_artist(request):
    try:
        resp = featuredartist.get_featured_artists(req_type=Names.API)
        return ResponseBack(code=resp.code, message=resp.message, data=resp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.FEATURED_ARTIST_FOUND_ERROR, data=str(e))
#function to add featured artist
@api_view(['GET'])
@permission_classes([AllowAny])
def add_featured_artist(request):
    try:
        resp = featuredartist.add_featured_artist()
        print("here")
        return ResponseBack(code=resp.code, message=resp.message, data=resp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.FEATURED_ARTIST_ADDED_ERROR, data=str(e))

@api_view(['GET'])
@permission_classes([AllowAny])
def get_featured_artist_by_genra(request,genra_id):
    try:
        resp = featuredartist.get_featured_artists_by_genra(genra_id=genra_id,req_type=Names.API)
        # print(resp)
        return ResponseBack(code=resp.code, message=resp.message, data=resp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.FEATURED_ARTIST_BY_GENRA_FOUND_ERROR, data=str(e))