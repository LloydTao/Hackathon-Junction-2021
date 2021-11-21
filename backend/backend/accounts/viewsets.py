from rest_framework import status, viewsets
from accounts.models.user import User
from accounts.serializers import (
    UserSerializer,
    UserLoginSerializer,
    UserLoginResponseSerializer,
)
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from django.middleware.csrf import get_token


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=False, methods=["post"])
    def login(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data["username"],
                password=serializer.validated_data["password"],
            )
            if user is not None:
                token = Token.objects.get_or_create(user=user)[0]
                return Response(
                    UserLoginResponseSerializer(
                        {
                            "id": user.id,
                            "username": user.username,
                            "token": token.key,
                        }
                    ).data
                )
            return Response(
                {"detail": "Invalid Username or Password"},
                status=status.HTTP_401_UNAUTHORIZED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=False, methods=["get"])
    def csrf(self, request):
        return Response({"token": get_token(request)})
