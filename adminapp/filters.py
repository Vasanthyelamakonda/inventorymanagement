import django_filters
from .models import *

class SearchFilter(django_filters.FilterSet):
    class meta:
        model=Dailysheet
        fields='__all__'