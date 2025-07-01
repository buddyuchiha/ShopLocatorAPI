from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from django_filters import rest_framework as filters
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View

from .filters import ShopFilter
from .models import City, Shop, Street
from .serializer import (
    GetShopSerializer,
    ShopSerializer,
    CitySerializer,
    StreetSerializer
)
# Create your views here.

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request')
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request')
    

class GetCity(ListAPIView):
    queryset = City.objects.all() 
    serializer_class = CitySerializer
    
class PostCity(CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    
class GetCityStreets(ListAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class PostStreet(CreateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class PostShop(CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def perfrom_create(self, serializer):
        obj = serializer.save()
        Response(obj.id)

  
class GetShop(ListAPIView):
    queryset = Shop.objects.all()
    serializer_class = GetShopSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ShopFilter 