from redpillmusicapp.UTILITY.ResponseBack import ResponseBack
from redpillmusicapp.MESSAGES.ResponseMessages import ResponseMessage
from redpillmusicapp.MESSAGES.ResponseCode import ResponseCode
from redpillmusicapp.CONTROLLERS.ARTISTCONTROLLERS.featuredartistcontroller import FeaturedArtistController
from redpillmusicapp.models import LastUpdated
featuredartist = FeaturedArtistController()
def is_featured_song_updated(todaydate):
    try:
        last_updated = LastUpdated.objects.all().first()
        if last_updated.featuredartist < todaydate:
            featresp = featuredartist.add_featured_artist()
            if featresp.code == ResponseCode.ERROR:
                return ResponseBack(code=ResponseCode.ERROR,message=ResponseMessage.FEATURED_ARTIST_ADDED_ERROR, data=featresp.data,local=True
                )
            last_updated.featuredartist = todaydate
            last_updated.save()

        return ResponseBack(code = ResponseCode.SUCCESS,message=ResponseMessage.CORON_PROCESS_SUCESS,data = [],local=True)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR,message=ResponseMessage.ARTIST_CORON_PROCESS_ERROR,data=str(e),local=True)