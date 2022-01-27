from rest_framework import viewsets
from apiservice import models
from apiservice import serializers
from apiservice import pagination
from apiservice.filters import ApiFilter, CollectionFilter


# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import filters


class CollectionView(viewsets.ModelViewSet):
    queryset = models.Collection.objects.all()
    serializer_class = serializers.CollectionSerializer
    pagination_class = pagination.Pagination

    # 在setting.py中定义了默认的filter_backends, 这里就不用重复配置了
    # filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = CollectionFilter
    ordering_fields = ('id', 'create_time', 'update_time')
    ordering = ('order',)


class ApiView(viewsets.ModelViewSet):
    queryset = models.Api.objects.all()
    serializer_class = serializers.ApiSerializer
    pagination_class = pagination.Pagination

    # filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    filter_class = ApiFilter
    ordering_fields = ('id', 'create_time', 'update_time')
    ordering = ('order',)


class CaseView(viewsets.ModelViewSet):
    queryset = models.Case.objects.all()
    serializer_class = serializers.CaseSerializer
    pagination_class = pagination.Pagination


class ResultView(viewsets.ModelViewSet):
    queryset = models.Result.objects.all()
    serializer_class = serializers.ResultSerializer
    pagination_class = pagination.Pagination
