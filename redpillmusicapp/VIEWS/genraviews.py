from redpillmusicapp.UTILITY.ResponseBack import ResponseBack
from redpillmusicapp.MESSAGES.ResponseMessages import ResponseMessage
from redpillmusicapp.MESSAGES.Names import Names
from redpillmusicapp.MESSAGES.ResponseCode import ResponseCode
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import AllowAny
from redpillmusicapp.CONTROLLERS.GENRACONTROLLERS.genracontroller import genracontrollers
Genracontroller = genracontrollers()
@api_view(['GET'])
@permission_classes([AllowAny])
def get_genra_by_id(request,genra_id):
    try:
        genraresp = Genracontroller.get_genra_by_id(genra_id=genra_id)
        return ResponseBack(code=genraresp.code,message=genraresp.message,data=genraresp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR,message=ResponseMessage.GENRA_FOUND_ERROR,data=str(e))

@api_view(['GET'])
@permission_classes([AllowAny])
def get_genras(request):
    try:
        genraresp = Genracontroller.get_genra()
        return ResponseBack(code = genraresp.code,message=genraresp.message,data = genraresp.data)
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR,message=ResponseMessage.ALL_GENRA_DATA_FOUND_ERROR,data=str(e))