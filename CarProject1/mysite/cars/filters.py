from django_filters import FilterSet
from .models import Car


class CarFilter(FilterSet):
    class Meta:
        model = Car
        fields = {
            'brand': ['exact'],
            'price': ['gt', 'lt']
        }