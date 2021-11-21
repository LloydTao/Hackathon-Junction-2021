from django.contrib.auth import get_user_model

from rest_framework import serializers
from messaging.models import Room, Message


class SussySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username"]


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

    sender = SussySerializer()

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
