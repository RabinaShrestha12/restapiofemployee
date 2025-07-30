from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
# from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

User = get_user_model()

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return{
        'refresh': str(refresh),
        'access': str(refresh.access_token)
    }

@api_view(['POST'])
@permission_classes([AllowAny])
def register_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    email = request.data.get('email')
    phone = request.data.get('phone')
    address=request.data.get('address')

    if User.objects.filter(username=username).exists():
       return Response({'err': "email is already exists and used another"},status=status.HTTP_400_BAD_REQUEST)
   
    try:
        User.objects.create_user(
            username=username,
            email=email,
            password=password,
            phone=phone,
            address=address
        )
        return Response({'msg': "User registered successfully."}, status=status.HTTP_201_CREATED)
    except Exception as e:
        return Response({'err': f"Failed to register user: {str(e)}"}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([AllowAny])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')
    
    if not username:
        return Response({'err':"username is required"})
    
    if not password:
        return Response({'err':"password is required"},status=status.HTTP_400_BAD_REQUEST)

    user = authenticate(username=username, password=password)
    if user is not None:
        tokens = get_tokens_for_user(user)
        return Response({'msg':"user login successfully", 'tokens':tokens}, status=status.HTTP_200_OK)
    
    else:
        return Response({'err':"Incorrect password"},status= status.HTTP_400_BAD_REQUEST)