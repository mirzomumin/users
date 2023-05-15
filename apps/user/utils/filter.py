import django_filters.rest_framework as filters
from django.contrib.auth.models import User


class UserFilters(filters.FilterSet):
    """
    Custom Filter for Users
    """
    first_name = filters.BaseInFilter('first_name')
    last_name = filters.BaseInFilter('last_name')

    class Meta:
        model = User
        fields = ('first_name', 'last_name')