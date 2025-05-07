from redpillmusicapp.MESSAGES.ResponseMessages import ResponseMessage
from redpillmusicapp.MESSAGES.Names import Names
from redpillmusicapp.MESSAGES.ResponseCode import ResponseCode
from redpillmusicapp.UTILITY.ResponseBack import ResponseBack
from redpillmusicapp.models import Genra


class genracontrollers():

    #get genra data
    def genra_data(self,genra):
        try:
            genradata = {
                Names.ID :genra.id,
                Names.GENRA_NAME: genra.genra_name
            }
            return ResponseBack(code=ResponseCode.SUCCESS,message=ResponseMessage.GENRA_FOUND_SUCCESS,data=genradata,local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR,message=ResponseMessage.GENRA_FOUND_ERROR,data=str(e),local=True)

    #Get genra by id
    def get_genra_by_id(self,genra_id):
        try:
            genra = Genra.objects.get(id = genra_id)
            genraresp = self.genra_data(genra=genra)
            return ResponseBack(code=genraresp.code,message=genraresp.message,data=genraresp.data,local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR,message=ResponseMessage.GENRA_FOUND_ERROR,data=str(e),local=True)
        
    #get genra
    def get_genra(self):
        try:
            genras = Genra.objects.all()
            allgenradata = []
            for genra in genras:
                genraresp = self.genra_data(genra=genra)
                genradata = {
                    Names.STATUS:genraresp.code,
                    Names.DATA:genraresp.data
                }
                allgenradata.append(genradata)

            return ResponseBack(code=ResponseCode.SUCCESS,message=ResponseMessage.ALL_GENRA_DATA_FOUND_SUCCESS,data=allgenradata,local=True)
        except Exception as e:
            return ResponseBack(code=ResponseCode.ERROR,message=ResponseMessage.ALL_GENRA_FOUND_ERROR,data=str(e),local=True)

