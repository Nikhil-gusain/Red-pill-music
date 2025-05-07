import dotsi
from rest_framework.response import Response

# d = dotsi.Dict({"foo": {"bar": "baz"}})
# d.foo.bar
# install dotsi and rest frame work

def ResponseBack(code='', message='', data={}, local=False):
    if local == True:
        obj = {
            'code': code,
            'message': message,
            'data': data,
        }
        model = dotsi.Dict(obj)
        return model
    if local == False:
        obj = {
            'code': code,
            'message': message,
            'data': data,
        }
        return Response(obj)