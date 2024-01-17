from rest_framework import serializers
from user.serializer import UserSerializer
from . import models
from .models import Favorite



class PartSerializer(serializers.ModelSerializer):
    user_added = UserSerializer(read_only=True)
    status = serializers.CharField(read_only=True)

    class Meta:
        model = models.Part

        fields = '__all__'


class PartLocationFilterSerializer(serializers.Serializer):
    user_lat = serializers.FloatField(required=False)
    user_lon = serializers.FloatField(required=False)
    max_radius = serializers.IntegerField(required=False)


class FavoriteSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.Favorite
        fields = '__all__'

class RatingSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)

    class Meta:
        model = models.Rating
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    user_added = UserSerializer(read_only=True)
    date_added = serializers.DateField(read_only=True, format='%d %B %Y')

    class Meta:
        model = models.Comment
        fields = (
            'user_added',
            'content',
            'date_added',
            'part',
        )
        write_only_fields = (
            'part',
        )
