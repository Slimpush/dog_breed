from django.shortcuts import get_object_or_404
from rest_framework import mixins, status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Breed, Dog
from .serializer import BreedSerializer, DogSerializer


def _save_object(serializer_class, request_data, instance=None):
    serializer = (
        serializer_class(instance, data=request_data)
        if instance
        else serializer_class(data=request_data)
    )
    if serializer.is_valid():
        serializer.save()
        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED if not instance else status.HTTP_200_OK,
        )
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogList(APIView):
    def get(self, request: Request) -> Response:
        dogs = Dog.objects.select_related('breed').all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        return _save_object(DogSerializer, request.data)


class DogDetail(APIView):
    def get(self, request: Request, pk: int) -> Response:
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request: Request, pk: int) -> Response:
        dog = get_object_or_404(Dog, pk=pk)
        return _save_object(DogSerializer, request.data, dog)

    def delete(self, request: Request, pk: int) -> Response:
        dog = get_object_or_404(Dog, pk=pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedList(
    mixins.CreateModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer


class BreedDetail(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet,
):
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer
