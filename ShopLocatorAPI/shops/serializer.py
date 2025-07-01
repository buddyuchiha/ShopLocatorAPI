from rest_framework import serializers
from .models  import Shop, City, Street

class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = [
                    "name", "city",
                    "street", "house",
                    "time_open", "time_close"
                 ]


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

