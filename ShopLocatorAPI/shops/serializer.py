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
    class Meta:
        model = Shop
        fields = [
                    "name", "city",
                    "street", "house",
                    "time_open", "time_close"
                 ]
        

class GetShopSerializer(ShopSerializer):
    city = serializers.CharField(source='city.name', read_only=True)
    street = serializers.CharField(source='street.name', read_only=True)

