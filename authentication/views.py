from . serializers import *
from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework import generics, permissions
from knox.models import AuthToken
from rest_framework.response import Response
from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

class LoginAPI(KnoxLoginView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [permissions.AllowAny]
    
    def post(self, request):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)
# API registration
class APIregister(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = SerializerRegister

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": SerializerUser(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })
        