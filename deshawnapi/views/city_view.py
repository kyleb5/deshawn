
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers, status
from deshawnapi.models import City


class CityView(ViewSet):

    def retrieve(self, request, pk=None):
        city = City.objects.get(pk=pk)
        serialized = CitySerializer(city, context={'request': request})
        return Response(serialized.data, status=status.HTTP_200_OK)

    def list(self, request):
        cities = City.objects.all()
        serialized = CitySerializer(cities, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('id', 'name',)
