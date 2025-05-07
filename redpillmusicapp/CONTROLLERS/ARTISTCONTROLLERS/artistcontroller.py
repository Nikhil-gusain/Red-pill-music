from redpillmusicapp.models import Artist,Genra,User
from redpillmusicapp.MESSAGES.ResponseMessages import ResponseMessage
from redpillmusicapp.MESSAGES.Names import Names
from redpillmusicapp.MESSAGES.ResponseCode import ResponseCode
from redpillmusicapp.UTILITY.ResponseBack import ResponseBack
import json

class ArtistController():

    #get all artist data
    def get_artists(self):
        try:
            #get data from request
            artists = Artist.objects.all()
            artist_data = []
            for artist in artists:
                artistresp = self.get_artists_data(artist)
                data = {
                    Names.STATUS:artistresp.code,
                    Names.DATA:artistresp.data
                }
                artist_data.append(data)
                
            return ResponseBack(code=ResponseCode.SUCCESS,
                                message=ResponseMessage.ARTIST_FOUND_SUCCESS,
                                data=artist_data,
                                local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR,
                                message=ResponseMessage.ARTIST_FOUND_ERROR,
                                data=str(e),
                                local=True)

    # function to get artist data
    def get_artists_data(self,artist):
        try:
            artist_data = {
                Names.ARTIST_ID:artist.id,
                Names.ARTIST_NAME:artist.artist_name,
                Names.ARTIST_CONTACT:artist.artist_contact,
                Names.ARTIST_DESCRIPTION:artist.description,
                Names.ARTIST_PROFILE_PIC:artist.profile_pic.url,
                Names.ARTIST_GENRA:artist.Genra.genra_name,
                Names.ARTIST_LINK:json.loads(artist.Links)
            }
            return ResponseBack(code=ResponseCode.SUCCESS,
                                message=ResponseMessage.ARTIST_DATA_FOUND_SUCCESS,
                                data=artist_data,
                                local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR,
                                message=ResponseMessage.ARTIST_DATA_FOUND_ERROR,
                                data=str(e),
                                local=True)

    # function to create artist
    def create_artist(self,request):
        try:
            #get data from request
            user = request.user
            artist_name = request.data.get(Names.ARTIST_NAME)
            artist_contact = request.data.get(Names.ARTIST_CONTACT)
            artist_description = request.data.get(Names.ARTIST_DESCRIPTION)
            artist_profile_pic = request.data.get(Names.ARTIST_PROFILE_PIC)
            spotify_links = request.data.get(Names.SPOTIFY_LINK, '')
            youtube_links = request.data.get(Names.YOUTUBE_LINK, '')
            instagram_links = request.data.get(Names.INSTAGRAM_LINK, '')
            artist_link = {
                Names.SPOTIFY:spotify_links,
                Names.YOUTUBE:youtube_links,
                Names.INSTAGRAM:instagram_links
            }


            artist_genra = request.data[Names.ARTIST_GENRA]if Names.ARTIST_GENRA in request.data else None
            genra = Genra.objects.get(genra_name =artist_genra)

            #create artist model and add data in it 
            artist = Artist()
            artist.user = user
            artist.artist_name = artist_name
            artist.artist_contact = artist_contact
            artist.description = artist_description
            artist.profile_pic = artist_profile_pic
            artist.Genra = genra
            artist.Links = json.dumps(artist_link)
            artist.save()

            return ResponseBack(code=ResponseCode.SUCCESS,
                                message=ResponseMessage.ARTIST_CREATED_SUCCESS,
                                data=artist,
                                local=True)
            pass
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, 
            message=ResponseMessage.ARTIST_CREATED_ERROR, 
            data=[],
            local=True)
    # function to upsate artist
    def update_artist(self,request,artist_id):
        try:
            #get data from request
            user = request.user
            artist = Artist.objects.get(id =artist_id)
            artist_user = artist.user
            if user != artist_user:
                return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.ONLY_ARTIST_CAN_UPDATE, data=[],local=True)

            artist_name = request.data.get(Names.ARTIST_NAME, artist.artist_name)
            artist_contact = request.data.get(Names.ARTIST_CONTACT, artist.artist_contact)
            artist_description = request.data.get(Names.ARTIST_DESCRIPTION, artist.description)

            links = json.loads(artist.Links)
            spotify_links = request.data.get(Names.SPOTIFY_LINK, links.get(Names.SPOTIFY, ''))
            youtube_links = request.data.get(Names.YOUTUBE_LINK, links.get(Names.YOUTUBE, ''))
            instagram_links = request.data.get(Names.INSTAGRAM_LINK, links.get(Names.INSTAGRAM, ''))

            artist_link = {
                Names.SPOTIFY:spotify_links,
                Names.YOUTUBE:youtube_links,
                Names.INSTAGRAM:instagram_links
            }
            artist_genra = request.data[Names.ARTIST_GENRA]if Names.ARTIST_GENRA in request.data else None
            genra = Genra.objects.get(genra_name =artist_genra)

            #Update artist
            
            artist.artist_name = artist_name
            artist.artist_contact = artist_contact
            artist.description = artist_description
            artist.Genra = genra
            artist.Links = json.dumps(artist_link)
            artist.save()

            return ResponseBack(code=ResponseCode.SUCCESS, 
            message=ResponseMessage.ARTIST_UPDATED_SUCCESS, 
            data=artist,
            local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, 
            message=ResponseMessage.ARTIST_UPDATED_ERROR, 
            data=[],
            local=True)
    # function to get artist
    def get_artist(self,artist_id,req_type):
        try:
            #get data from request
            artist = Artist.objects.get(id =artist_id)

            artistresp = self.get_artists_data(artist,req_type=req_type)
            
            return ResponseBack(code=artistresp.code, 
            message=artistresp.message, 
            data=artistresp.data,
            local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, 
            message=ResponseMessage.ARTIST_FOUND_ERROR, 
            data=[],
            local=True)
    #function to get artist by genra
    def get_artists_by_genra(self,genra_id,req_type):
        try:
            #get data from request
            genra = Genra.objects.get(id =genra_id)
            artists = genra.genra_artists.all()
            artist_data = []
            for artist in artists:
                artistresp = self.get_artists_data(artist,req_type=req_type)
                data = {Names.STATUS:artistresp.code,Names.DATA:artistresp.data}
                artist_data.append(data)
            return ResponseBack(code=ResponseCode.SUCCESS, message=ResponseMessage.ARTIST_FOUND_SUCCESS, data=artist_data,local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.ARTIST_FOUND_ERROR, data=str(e),local=True)
    #function to delete artist
    def delete_artist(self,artist_id):
        try:
            #get data from request
            artist = Artist.objects.get(id =artist_id)
            artist.delete()
            return ResponseBack(code=ResponseCode.SUCCESS, 
            message=ResponseMessage.ARTIST_DELETED_SUCCESS, 
            data=[],
            local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR, 
            message=ResponseMessage.ARTIST_DELETED_ERROR, 
            data=[],
            local=True)
        pass