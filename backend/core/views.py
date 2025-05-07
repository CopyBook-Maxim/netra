from rest_framework import viewsets, permissions
from .models import ConfigTemplate
from .serializers import ConfigTemplateSerializer

class ConfigTemplateViewSet(viewsets.ModelViewSet):
    queryset = ConfigTemplate.objects.all()
    serializer_class = ConfigTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]
