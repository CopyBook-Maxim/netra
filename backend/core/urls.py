from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import ConfigTemplateViewSet

router = DefaultRouter()
router.register(r'templates', ConfigTemplateViewSet, basename='template')

urlpatterns = [
    path('', include(router.urls)),
]
