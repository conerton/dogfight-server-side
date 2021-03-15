"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from dogfightapi.models import UserHotDog


class UserHotDogs(ViewSet):
    """Level up game types"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for single game type

        Returns:
            Response -- JSON serialized game type
        """
        try:
            user_hot_dog = UserHotDog.objects.get(pk=pk)
            serializer = UserHotDogSerializer(
                user_hot_dog, context={'request': request})
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        user_hot_dogs = UserHotDog.objects.all()

        # Note the addtional `many=True` argument to the
        # serializer. It's needed when you are serializing
        # a list of objects instead of a single object.
        serializer = UserHotDogSerializer(
            user_hot_dogs, many=True, context={'request': request})
        return Response(serializer.data)


class UserHotDogSerializer(serializers.ModelSerializer):
    """JSON serializer for game types

    Arguments:
        serializers
    """
    class Meta:
        model = UserHotDog
        fields = ('id', 'user', 'hot_dog', 'date_completed',
                  'is_favorite', 'note', 'is_approved')
