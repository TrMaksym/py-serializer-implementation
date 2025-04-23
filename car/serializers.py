from rest_framework import serializers
from car.models import Car

class CarSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    manufacturer = serializers.CharField(max_length=64)
    model = serializers.CharField(max_length=64)
    horse_powers = serializers.IntegerField(min_value=1, max_value=1000)
    is_broken = serializers.BooleanField(default=False)
    problem_description = serializers.CharField(allow_blank=True, allow_null=True, required=False)

    def validate_manufacturer(self, value):
        if len(value) > 64:
            raise serializers.ValidationError("Manufacturer name must be 64 characters or less.")
        return value

    def validate_model(self, value):
        if len(value) > 64:
            raise serializers.ValidationError("Model name must be 64 characters or less.")
        return value

    def validate_horse_powers(self, value):
        if not (1 <= value <= 1000):
            raise serializers.ValidationError("Horse powers must be between 1 and 1000.")
        return value

    def create(self, validated_data):
        return Car.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.manufacturer = validated_data.get('manufacturer', instance.manufacturer)
        instance.model = validated_data.get('model', instance.model)
        instance.horse_powers = validated_data.get('horse_powers', instance.horse_powers)
        instance.is_broken = validated_data.get('is_broken', instance.is_broken)
        instance.problem_description = validated_data.get('problem_description', instance.problem_description)
        instance.save()
        return instance