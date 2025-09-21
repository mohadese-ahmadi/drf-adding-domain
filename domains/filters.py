import django_filters
from .models import Domain

class DomainFilter(django_filters.FilterSet):
    created_from = django_filters.DateTimeFilter(field_name="createdDate", lookup_expr='gte')
    created_to   = django_filters.DateTimeFilter(field_name="createdDate", lookup_expr='lte')

    class Meta:
        model = Domain
        fields = ['status', 'isActive', 'created_from', 'created_to']
