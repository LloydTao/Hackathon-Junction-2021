from rest_framework import serializers
from messaging.models import Room, Message


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = [
            "id",
            "name",
            "users",
            "messages",
        ]


class MessagePostSerializer(serializers.Serializer):
    class Meta:
        model = Message
        fields = [
            "content",
        ]


class MessageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Message
        fields = [
            "id",
            "room",
            "sender",
            "content",
            "flagged",
            "flags",
            "likes",
        ]
