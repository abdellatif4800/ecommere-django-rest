from django.shortcuts import render
from django.contrib.auth import authenticate

from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed

from . import serializer


class UserRegiester(CreateAPIView):
    serializer_class = serializer.UserSerializer
    queryset = User.objects.all()


class Signin(APIView):
    def post(self, request):
        user = authenticate(
            username=request.data["username"], password=request.data["password"]
        )
        if not user.is_active:
            raise AuthenticationFailed("Invalid credentials")
        refresh = RefreshToken.for_user(user)

        return Response(
            {
                # "user": serializer.UserSerializer(user).data,
                "refresh": str(refresh),
                "access": str(refresh.access_token),
            }
        )
