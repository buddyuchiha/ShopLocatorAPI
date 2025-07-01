from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView
from django.views.generic.edit import CreateView

from .models import City, Shop, Street
from .serializer import ShopSerializer, CitySerializer, StreetSerializer
# Create your views here.

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request')
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request')
    

class GetCity(ListAPIView):
    queryset = City.objects.all() 
    serializer_class = CitySerializer
    
    
class GetCityStreets(ListAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer

    
class PostCity(CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class PostStreet(CreateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class PostShop(CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

  
    