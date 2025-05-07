from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from redpillmusicapp.MESSAGES.ResponseMessages import ResponseMessage
from redpillmusicapp.MESSAGES.Names import Names
from redpillmusicapp.MESSAGES.ResponseCode import ResponseCode
from redpillmusicapp.UTILITY.ResponseBack import ResponseBack
@api_view(['POST'])
@permission_classes([AllowAny])
def api_register(request):
    try:
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if User.objects.filter(username=username).exists():
            return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.USERNAME_ALREADY_EXISTS, data=[]) 

        user = User.objects.create_user(username=username, email=email, password=password)

        refresh = RefreshToken.for_user(user)

        return ResponseBack(code=ResponseCode.SUCCESS, message=ResponseMessage.USER_CREATED_SUCCESS, data={'refresh': str(refresh), 'access': str(refresh.access_token), 'username': user.username})
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.USER_CREATED_ERROR, data=[])


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def my_protected_view(request):
    try:
        return ResponseBack(code=ResponseCode.SUCCESS, message=ResponseMessage.USER_FOUND_SUCCESS, data={'username': request.user.username})
    except Exception as e:
        return ResponseBack(code=ResponseCode.ERROR, message=ResponseMessage.USER_FOUND_ERROR, data=[])
    
@api_view(['POST'])
@permission_classes([AllowAny])
def custom_login(request):
    try:
        username = request.data.get(Names.USERNAME)
        password = request.data.get(Names.PASSWORD)

        if not username or not password:
            return ResponseBack(
                code=ResponseCode.ERROR,
                message=ResponseMessage.CREDENTIALS_REQUIRED,
                local=False
            )

        user = authenticate(username=username, password=password)

        if user is None:
            return ResponseBack(
                code=ResponseCode.UNAUTHORIZED,
                message=ResponseMessage.INVALID_CREDENTIALS,
                local=False
            )

        refresh = RefreshToken.for_user(user)
        token_data = {
            Names.REFRESH_TOKEN: str(refresh),
            Names.ACCESS_TOKEN: str(refresh.access_token),
        }

        return ResponseBack(
            code=ResponseCode.SUCCESS,
            message=ResponseMessage.LOGIN_SUCCESS,
            data=token_data,
            local=False
        )

    except Exception as e:
        return ResponseBack(
            code=ResponseCode.ERROR,
            message=ResponseMessage.LOGIN_ERROR,
            data=[str(e)],
            local=False
        )
