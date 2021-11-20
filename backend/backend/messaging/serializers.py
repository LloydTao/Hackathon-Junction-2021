from rest_framework import serializers
from messaging.models import Room, Message


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Room
        fields = [
            "id",
            "name",
            "users",
        ]


class RoomUsersSerializer(serializers.Serializer):
    user_ids = serializers.ListField(child=serializers.IntegerField())


class MessagePostSerializer(serializers.ModelSerializer):
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
            "created",
        ]
