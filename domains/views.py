from django.shortcuts import render

from rest_framework import viewsets

from .models import Domain
from .serializers import DomainSerializer
# Create your views here.


class DomainViewSets(viewsets.ModelViewSet):
    queryset = Domain.objects.all().order_by("createdDate")
    serializer_class = DomainSerializer