from typing import Optional

from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Breed, Dog
from .serializer import BreedSerializer, DogSerializer


class DogList(APIView):
    def get(self, request: Request) -> Response:
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetail(APIView):
    def get(self, request: Request, pk: int) -> Response:
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request: Request, pk: int) -> Response:
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: int) -> Response:
        dog = get_object_or_404(Dog, pk=pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedDetail(viewsets.ViewSet):
    def get(self, request: Request, pk: Optional[int] = None) -> Response:
        breed = get_object_or_404(Breed, pk=pk)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    def put(self, request: Request, pk: Optional[int] = None) -> Response:
        breed = get_object_or_404(Breed, pk=pk)
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request: Request, pk: Optional[int] = None) -> Response:
        breed = get_object_or_404(Breed, pk=pk)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedList(viewsets.ViewSet):
    def get(self, request: Request) -> Response:
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    def post(self, request: Request) -> Response:
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
