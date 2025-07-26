from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import permissions
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import status

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

    if User.objects.filter(username=username).exists():
        return Response({'err':"email is already exists and used another"})
    try:
        User.objects.create_user(
            username = username,
            email = email,
            password = password
        )
        return Response({'msg':"user register successfully"}, status=status.HTTP_200_OK)
    except:
        return Response({'err': "Failed to Register user"}, status=status.HTTP_400_BAD_REQUEST)