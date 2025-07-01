from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import View, ListView

# Create your views here.

class MyView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET request')
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('POST request')
    

class GetCity(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET GetCity request')
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('POST GetCity request')
    
class GetCityStreets(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET GetCityStreets request')
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('POST GetCityStreets request')
    

class PostShop(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('GET PostShop request')
    
    def post(self, request, *args, **kwargs):
        return HttpResponse('POST PostShop request')
    