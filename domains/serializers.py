import re
from rest_framework import serializers
from .models import Domain
from django.contrib import sitemaps
class DomainSerializer(serializers.ModelSerializer):
    class Meta:
        model=Domain
        fields=['id','domain', 'isActive', 'status', 'createdDate']
        read_only_fields=['id', 'createdDate']
        
    def validate_domain(self, value):
        pattern=re.compile(
            r'^(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z0-9][a-z0-9-]{0,61}[a-z0-9]$',
            re.IGNORECASE,
        )
        if not pattern.fullmatch(value):
            raise serializers.ValidationError('Enter a valid domain for example www.google.com')
        return value