from django.contrib.auth.models import User
from . models import Lot
import django_filters

class ProductFilter(django_filters.FilterSet):
    
    class Meta:
        model = Lot
        fields = ['base_price','category','seller','is_live']
