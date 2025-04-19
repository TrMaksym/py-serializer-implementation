from rest_framework import serializers

from car.models import Car


class CarSerializer(serializers.Serializer):
    class Meta:
        model = Car
        field = ["model, horse_power, manufacturer"]

