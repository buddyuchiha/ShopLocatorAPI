from django.urls import path, re_path, register_converter
from . import views

urlpatterns = [
    path('', views.MyView.as_view(), name='home'),
    path('city/', views.GetCity.as_view(), name='cities'),
    path('city/street/', views.GetCityStreets.as_view(), name='streets'),
    path('shop/', views.PostShop.as_view(), name='shops'),
]