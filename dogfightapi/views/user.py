from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from dogfightapi.models import UserHotDog, HotDog
from django.contrib.auth import get_user_model
from django.db.models import Count
from django.contrib.auth.models import User


class Users(ViewSet):

    def list(self, request):
        """Handle GET requests to get all user types

        Returns:
            Response -- JSON serialized list of user types
        """

        users = User.objects.annotate(hotdog_count=Count(
            'hotdogs')).filter(hotdog_count__gte=37)

        serializer = UserSerializer(
            users, many=True, context={'request': request})
        return Response(serializer.data)


class UserSerializer(serializers.ModelSerializer):
    """JSON serializer for u_hot_dog types

    Arguments:
        serializers
    """
    class Meta:
        model = User
        fields = ('id', 'password', 'last_login', 'is_superuser',
                  'username', 'last_name', 'email', 'is_staff', 'date_joined', 'first_name')
        depth = 1
