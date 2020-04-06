from rest_framework import serializers
from cars.models import *


class CarListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('vin', 'color', 'brand', 'car_type')


class CarDetailSerializer(serializers.ModelSerializer):
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Car
        fields = '__all__'
