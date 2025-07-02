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


class BaseListAPIView(ListAPIView):
      def handle_exception(self, exc):
        return Response({'data': 'Incorrect request'}, status=400)
    

class MyView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'shops/home_view.html')
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request')
    

class GetCity(BaseListAPIView):
    queryset = City.objects.all() 
    serializer_class = CitySerializer
    

class PostCity(CreateAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer

    
class GetCityStreets(BaseListAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer
    def get_queryset(self):
        city_id = self.kwargs['city_id'] 
        return Street.objects.filter(city_id=city_id)


class PostStreet(CreateAPIView):
    queryset = Street.objects.all()
    serializer_class = StreetSerializer


class PostShop(CreateAPIView):
    queryset = Shop.objects.all()
    serializer_class = ShopSerializer

    def perfrom_create(self, serializer):
        obj = serializer.save()
        Response(obj.id)

  
class GetShop(BaseListAPIView):
    queryset = Shop.objects.all()
    serializer_class = GetShopSerializer
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ShopFilter 