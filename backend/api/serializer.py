from rest_framework import serializers

from .models import Breed, Dog


class DogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dog
        fields = "__all__"

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["breed"] = instance.breed.name
        return representation


class BreedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = "__all__"
