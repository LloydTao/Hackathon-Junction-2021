from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from messaging.models import Room, Message
from messaging.serializers import RoomSerializer, RoomUsersSerializer, MessageSerializer, MessagePostSerializer
from accounts.serializers import UserSerializer
from accounts.models.user import User


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    def get_queryset(self):
        return Room.objects.all().filter(users=self.request.user)


    @action(detail=True, methods=["get", "post"])
    def messages(self, request, pk=None):
        room = self.get_object()
        if request.method == "POST":
            print(request.data)
            serializer = MessagePostSerializer(data=request.data)
            if serializer.is_valid():
                print(dict(serializer.validated_data))
                new_message = room.messages.create(
                    content=serializer.validated_data["content"],
                    sender=request.user,
                )
                return Response(MessageSerializer(new_message, context={"request": request}).data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print(room.messages)
        return Response(
            MessageSerializer(
                room.messages.all(), many=True, context={"request": request}
            ).data
        )

    @action(detail=True, methods=['get', 'post'])
    def users(self, request, pk=None):
        room = self.get_object()
        if request.method == "POST":
            serializer = RoomUsersSerializer(data=request.data)
            if serializer.is_valid():
                user_list = User.objects.all().filter(id__in=serializer.validated_data['user_ids']).values_list('id', flat=True)
                new_users = room.users.add(*user_list)
                return Response(UserSerializer(room.users, many=True, context={"request": request}).data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(UserSerializer(room.users, many=True, context={"request": request}).data)



class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer

    
    def get_queryset(self):
        return Message.objects.all().filter(room__users=self.request.user)

    @action(detail=True, methods=['post'])
    def flag(self, request, pk=None):
        message = self.get_object()
        if message.sender == request.user:
            return Response({'detail': 'You cannot flag your own messages'}, status=status.HTTP_400_BAD_REQUEST)
        message.flags += 1
        message.save()
        return Response(MessageSerializer(message, context={"request": request}).data)

    @action(detail=True, methods=['post'])
    def like(self, request, pk=None):
        message = self.get_object()
        if message.sender == request.user:
            return Response({'detail': 'You cannot like your own messages'}, status=status.HTTP_400_BAD_REQUEST)
        message.likes += 1
        message.save()
        return Response(MessageSerializer(message, context={"request": request}).data)


