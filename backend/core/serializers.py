from rest_framework import serializers
from .models import ConfigTemplate

class ConfigTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ConfigTemplate
        fields = '__all__'
