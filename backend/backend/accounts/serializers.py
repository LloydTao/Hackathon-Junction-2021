from rest_framework import serializers
from accounts.models.user import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
        ]


class UserLoginResponseSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    username = serializers.CharField()
    token = serializers.CharField()


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
