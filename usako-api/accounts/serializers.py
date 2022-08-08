from rest_framework import serializers
from .models import Space, User


class SpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Space
        fields = "__all__"
        read_only_fields = ("id",)
        extra_kwargs = {
            "password": {
                "write_only": True,
            }
        }


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        read_only_fields = ("id",)


class LinkAccountSpaceSerializer(serializers.Serializer):
    line_id = serializers.CharField(max_length=128)
    space_name = serializers.CharField(max_length=128)
    password = serializers.CharField(max_length=128)
