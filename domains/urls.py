from django.urls import path, include

from .views import DomainViewSets

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Domain', DomainViewSets, basename='domain')

urlpatterns = [
    path('', include(router.urls)),
]