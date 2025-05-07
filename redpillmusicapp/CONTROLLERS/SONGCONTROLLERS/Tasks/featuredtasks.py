from redpillmusicapp.UTILITY.ResponseBack import ResponseBack
from redpillmusicapp.MESSAGES.ResponseMessages import ResponseMessage
from redpillmusicapp.MESSAGES.Names import Names
from redpillmusicapp.MESSAGES.ResponseCode import ResponseCode
from redpillmusicapp.CONTROLLERS.SONGCONTROLLERS.featuredsongcontroller import FeaturedSongController
from redpillmusicapp.models import LastUpdated
import datetime
featuredsongcontrollers = FeaturedSongController()
def is_featured_song_updated(todaydate):
    try:
        last_updated = LastUpdated.objects.all().first()

        if last_updated.featuredsong < todaydate:
            featresp = featuredsongcontrollers.add_featured_song()
            if featresp.code == ResponseCode.ERROR:
                return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.FEATURED_SONG_ADDED_ERROR, data=featresp.data,local=True
                )
            last_updated.featuredsong = todaydate
            last_updated.save()

        return ResponseBack(code = ResponseCode.SUCCESS,message=ResponseMessage.CORON_PROCESS_SUCESS,data = [],local=True)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR,message=ResponseMessage.SONG_CORON_PROCESS_ERROR,data=str(e),local=True)