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
        user_hot_dogs = UserHotDog.objects.all()

        sort_parameter = self.request.query_params.get('sortby', None)

        if sort_parameter is not None and sort_parameter == 'user':
            user = User.objects.get(pk=request.auth.user.id)
            user_hot_dogs = UserHotDog.objects.filter(
                user=user)

            serializer = UserHotDogSerializer(
                user_hot_dogs, many=True, context={'request': request})

        print(user_hot_dogs.query)

        # Note the addtional `many=True` argument to the
        # serializer. It's needed when you are serializing
        # a list of objects instead of a single object.

        # hot_dog = self.request.query_params.get('hot_dog_id', None)
        # if hot_dog is not None:
        #     user_hot_dogs = user_hot_dogs.filter(hot_dog__id=hot_dog)

        # user_name = self.request.query_params.get('user_id', None)
        # if user_name is not None:
        #     user_hot_dogs = user_hot_dogs.filter(user__id=user_name)

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

    def update(self, request, pk=None):
        """Handle PUT requests for a task
        Returns:
            Response -- Empty body with 204 status code
        """

        # sort_parameter = self.request.query_params.get('sortby', None)

        # if sort_parameter is not None and sort_parameter == 'user':
        #     user = User.objects.get(pk=request.auth.user.id)
        #     user_hot_dogs = UserHotDog.objects.filter(
        #         user=user)

        #     serializer = UserHotDogSerializer(
        #         user_hot_dogs, many=True, context={'request': request})

        # Grab data from client's request to build a new task instance
        user_hot_dog = UserHotDog.objects.get(pk=pk)
        user_hot_dog.hotdogs = request.auth.user
        # user_hot_dog.date_completed = request.data["dateCompleted"]
        user_hot_dog.is_favorite = request.data["isFavorite"]
        user_hot_dog.note = request.data["note"]
        # user_hot_dog.is_approved = request.data["isApproved"]
        # user_hot_dog.is_complete = request.data["isComplete"]
        # user_hot_dog.hot_dog = HotDog.objects.get(pk=request.data["hotDogId"])

        # Save the updated task instance to database,
        # overwriting the original values.
        user_hot_dog.save()

        return Response({}, status=status.HTTP_204_NO_CONTENT)

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
