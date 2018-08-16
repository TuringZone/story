from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from django.contrib.auth.models import User
from rest_framework.response import Response
from knox.models import AuthToken
from .models import UserProfile
from .serializers import UserSerializer, UserProfileSerializer, LoginUserSerializer

# Create your views here.

class UserViewset(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class UserProfileViewset(viewsets.ModelViewSet):
    serializer_class = UserProfileSerializer
    queryset = UserProfile.objects.all()
    lookup_field = 'user__username'

class LoginAPI(generics.GenericAPIView):
    serializer_class = LoginUserSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data
        try:
            tokens = AuthToken.objects.filter(user=user.id).delete()
            token = AuthToken.objects.create(user)
        except:
            token = AuthToken.objects.create(user)
        return Response({
            'user': UserSerializer(user, context=self.get_serializer_context()).data,
            'token': token
        })

class LogoutAPI(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    def get(self, request, *args, **kwargs):
        AuthToken.objects.filter(user=request.user.id).delete()
        return Response({'str': 'logged_out'})

class UserAPI(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user
