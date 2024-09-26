from models import Dog, Breed
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from serializer import DogSerializer, BreedSerializer
from rest_framework import status, viewsets
from rest_framework.views import APIView


class DogList(APIView):
    def get(self, request):
        dogs = Dog.objects.all()
        serializer = DogSerializer(dogs, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = DogSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class DogDetail(APIView):
    def get(self, request, pk):
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog)
        return Response(serializer.data)

    def put(self, request, pk):
        dog = get_object_or_404(Dog, pk=pk)
        serializer = DogSerializer(dog, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        dog = get_object_or_404(Dog, pk=pk)
        dog.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedDetail(viewsets.ViewSet):
    def get(self, request, pk=None):
        breed = get_object_or_404(Breed, pk=pk)
        serializer = BreedSerializer(breed)
        return Response(serializer.data)

    def put(self, request, pk=None):
        breed = get_object_or_404(Breed, pk=pk)
        serializer = BreedSerializer(breed, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk=None):
        breed = get_object_or_404(Breed, pk=pk)
        breed.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class BreedList(viewsets.ViewSet):
    def get(self, request):
        breeds = Breed.objects.all()
        serializer = BreedSerializer(breeds, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = BreedSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.date, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
