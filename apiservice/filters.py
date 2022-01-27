import django_filters
from apiservice.models import Api, Collection


class ApiFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    url = django_filters.CharFilter(field_name='url', lookup_expr='icontains')

    class Meta:
        model = Api
        fields = ('name', 'url',)


class CollectionFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')

    class Meta:
        model = Collection
        fields = ('name',)
