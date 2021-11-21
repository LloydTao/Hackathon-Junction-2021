from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from messaging.models import Room, Message
from messaging.serializers import (
    RoomSerializer,
    RoomUsersSerializer,
    MessageSerializer,
    MessagePostSerializer,
)
from accounts.serializers import UserSerializer
from accounts.models.user import User
import requests
import json


JUPYTER_HOST = "http://localhost:8889"


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.all().filter(users=self.request.user.id)

    @action(detail=True, methods=["get", "post"])
    def messages(self, request, pk=None):
        room = self.get_object()
        if request.method == "POST":
            serializer = MessagePostSerializer(data=request.data)
            if serializer.is_valid():
                # Check content for profanity
                req = requests.get(f"{JUPYTER_HOST}/predict", params={"string": serializer.validated_data["content"]})
                if req.status_code != 200:
                    return Response({}, status=status.HTTP_502_BAD_GATEWAY)
                # Get response data
                response = json.loads(req.text)
                # Create message with safe content
                new_message = room.messages.create(
                    content=response['prediction'],
                    sender=request.user,
                    flagged=response['offensive'] == "true",
                )
                return Response(
                    MessageSerializer(new_message, context={"request": request}).data
                )
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print(room.messages)
        return Response(
            MessageSerializer(
                room.messages.all(), many=True, context={"request": request}
            ).data
        )

    @action(detail=True, methods=["get", "post"])
    def users(self, request, pk=None):
        room = self.get_object()
        if request.method == "POST":
            serializer = RoomUsersSerializer(data=request.data)
            if serializer.is_valid():
                user_list = (
                    User.objects.all()
                    .filter(id__in=serializer.validated_data["user_ids"])
                    .values_list("id", flat=True)
                )
                new_users = room.users.add(*user_list)
                return Response(
                    UserSerializer(
                        room.users, many=True, context={"request": request}
                    ).data
                )
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(
            UserSerializer(room.users, many=True, context={"request": request}).data
        )


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.all().filter(room__users=self.request.user.id)

    @action(detail=True, methods=["post"])
    def flag(self, request, pk=None):
        message = self.get_object()
        if message.sender == request.user:
            return Response(
                {"detail": "You cannot flag your own messages"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        message.flags += 1
        message.save()
        # Tell ML Model to update
        req = requests.post(f"{JUPYTER_HOST}/add_data", data={'body': message.content})
        print(req.text)
        print(req.status_code)
        if req.status_code != 200:
            return Response(
                MessageSerializer(message, context={"request": request}).data,
                status=status.HTTP_502_BAD_GATEWAY
            )
        return Response(MessageSerializer(message, context={"request": request}).data)

    @action(detail=True, methods=["post"])
    def like(self, request, pk=None):
        message = self.get_object()
        if message.sender == request.user:
            return Response(
                {"detail": "You cannot like your own messages"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        message.likes += 1
        message.save()
        return Response(MessageSerializer(message, context={"request": request}).data)
