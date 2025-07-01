from rest_framework import serializers
from .models  import Shop, City, Street

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City 
        fields = [
                    "name"
                 ]


class StreetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Street 
        fields = [
                    "name", "city"
                 ]


class ShopSerializer(serializers.ModelSerializer):
    city = serializers.CharField(source='city.name')
    street = serializers.CharField(source='street.name')
    class Meta:
        model = Shop
        fields = [
                    "name", "city",
                    "street", "house",
                    "time_open", "time_close"
                 ]
