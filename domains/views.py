from django.shortcuts import render

from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend

from .models import Domain
from .serializers import DomainSerializer
# Create your views here.


class DomainViewSets(viewsets.ModelViewSet):
    queryset = Domain.objects.all().order_by("-createdDate")
    serializer_class = DomainSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['isActive', 'status']
    search_fields = ['domain']
    ordering_fields = ['createdDate', 'domain']