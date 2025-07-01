from django.urls import path, re_path, register_converter

from . import views

urlpatterns = [
    path('', views.MyView.as_view(), name='home'),
    path('city/', views.GetCity.as_view(), name='cities'),
    path('city/create/', views.PostCity.as_view(), name='create-cities'),
    path('city/street/', views.GetCityStreets.as_view(), name='streets'),
    path('city/<int:city_id>/street/create/', views.PostStreet.as_view(), name='create-streets'),
    path('shop/create/', views.PostShop.as_view(), name='create-shops'),
    path('shop/', views.GetShop.as_view(), name='shops')
]