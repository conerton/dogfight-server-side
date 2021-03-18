"""View module for handling requests about game types"""
from django.http import HttpResponseServerError
from django.core.exceptions import ValidationError
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from dogfightapi.models import UserHotDog, HotDog
from django.contrib.auth.models import User


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
        except UserHotDog.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all game types

        Returns:
            Response -- JSON serialized list of game types
        """
        user = User.objects.get(pk=request.auth.user.id)
        user_hot_dogs = UserHotDog.objects.filter(
            user=user)

        print(user_hot_dogs.query)

        # Note the addtional `many=True` argument to the
        # serializer. It's needed when you are serializing
        # a list of objects instead of a single object.


# reference code that doesn't make much sense at the moment
        # order = self.request.query_params.get('order_by', None)

        # if order is not None:
        #     order_filter = order

        #     if direction is not None:
        #         if direction == "desc":
        #             order_filter = f'-{order}'

        #     products = products.order_by(order_filter)

        hot_dog = self.request.query_params.get('hot_dog_id', None)
        if hot_dog is not None:
            user_hot_dogs = user_hot_dogs.filter(hot_dog__id=hot_dog)

        serializer = UserHotDogSerializer(
            user_hot_dogs, many=True, context={'request': request})
        return Response(serializer.data)

    def create(self, request):
        """Handle POST operations

        Returns:
            Response -- JSON serialized hot dog instance
        """

        # Uses the token passed in the `Authorization` header

        # Create a new Python instance of the Game class
        # and set its properties from what was sent in the
        # body of the request from the client.
        u_hot_dog = UserHotDog()
        u_hot_dog.date_completed = request.data["dateCompleted"]

        u_hot_dog.is_favorite = request.data["isFavorite"]
        u_hot_dog.note = request.data["note"]
        u_hot_dog.is_approved = request.data["isApproved"]

        # Use the Django ORM to get the record from the database
        # whose `id` is what the client passed as the
        # `gameTypeId` in the body of the request.
        u_hot_dog.hot_dog = HotDog.objects.get(pk=request.data["hotDogId"])

        u_hot_dog.user = request.auth.user

        # u_hot_dog.user = User.objects.get(user=request.auth.user)

        # Try to save the new u_hot_dog to the database, then
        # serialize the u_hot_dog instance as JSON, and send the
        # JSON as a response to the client request
        try:
            u_hot_dog.save()
            serializer = UserHotDogSerializer(
                u_hot_dog, context={'request': request})
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        # If anything went wrong, catch the exception and
        # send a response with a 400 status code to tell the
        # client that something was wrong with its request data
        except ValidationError as ex:
            return Response({"reason": ex.message}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        """Handle DELETE requests for a single game

        Returns:
            Response -- 200, 404, or 500 status code
        """
        try:
            u_hot_dog = UserHotDog.objects.get(pk=pk)
            u_hot_dog.delete()

            return Response({}, status=status.HTTP_204_NO_CONTENT)

        except UserHotDog.DoesNotExist as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_404_NOT_FOUND)

        except Exception as ex:
            return Response({'message': ex.args[0]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserHotDogSerializer(serializers.ModelSerializer):
    """JSON serializer for u_hot_dog types

    Arguments:
        serializers
    """
    class Meta:
        model = UserHotDog
        fields = ('id', 'user', 'hot_dog', 'date_completed',
                  'is_favorite', 'note', 'is_approved')
        depth = 2
