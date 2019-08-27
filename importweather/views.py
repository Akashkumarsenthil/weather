from django.shortcuts import render

from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import weatherdata
from .serializers import weatherdataserializer
from django.http import Http404

from rest_framework.filters import(
    SearchFilter,
    OrderingFilter,
)

from django.db.models import Q


# Create your views here.

class weatherList(APIView):
    def get(self, request , *args , **kwargs):
        weather = weatherdata.objects.all()
        serializer = weatherdataserializer(weather,  many=True)
        return Response(serializer.data)
    def post(self, request):
        serializer = weatherdataserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class weatherDetail(APIView):
    def get_object(self, city_name):
        try:
            return weatherdata.objects.filter(city_name__icontains=city_name)
        except Snippet.DoesNotExist:
            raise Http404

    def get(self, request, city_object, format=None):
        snippet = self.get_object(city_object.city_name)
        serializer = weatherdataserializer(snippet)
        return Response(serializer.data)



