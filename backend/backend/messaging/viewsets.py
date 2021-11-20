from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from messaging.models import Room, Message
from messaging.serializers import RoomSerializer, MessageSerializer


class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    @action(detail=True, methods=["get", "post"])
    def messages(self, request, pk=None):
        room = self.get_object()
        if request.method == "POST":
            serializer = MessagePostSerializer(data=request.data)
            if serializer.is_valid():
                room.messages.create(
                    content=serializer.validated_data["content"],
                    room=room,
                    sender=request.user,
                )
                return Response(serializer.data)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        print(room.messages)
        return Response(
            MessageSerializer(
                room.messages.all(), many=True, context={"request": request}
            ).data
        )


class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
