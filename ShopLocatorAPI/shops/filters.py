from django_filters import rest_framework as filters
from django.utils import timezone

from .models import City, Shop


class ShopFilter(filters.FilterSet):
    city = filters.NumberFilter(field_name='street__city__id')  
    street = filters.NumberFilter(field_name='street__id')   
    open = filters.NumberFilter(method='filter_by_open_status')

    class Meta:
        model = Shop
        fields = ['city', 'street', 'open']

    def filter_by_open_status(self, queryset, name, value):
        current_time = timezone.now().time()  

        if value == 1:  
            return queryset.filter(
                time_open__lte=current_time,
                time_close__gte=current_time
            )
        elif value == 0:  
            return queryset.exclude(
                time_open__lte=current_time,
                time_close__gte=current_time
            )
        
        return queryset