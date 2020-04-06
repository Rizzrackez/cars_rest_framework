from django.shortcuts import render
from rest_framework import generics
from cars.serializers import *
from cars.models import *
from cars.permissions import *
from rest_framework.authentication import TokenAuthentication


class CarCreateView(generics.CreateAPIView):
    serializer_class = CarDetailSerializer


class CarListView(generics.ListAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()


class CarDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = CarListSerializer
    queryset = Car.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsOwnerOrReadOnly, )


