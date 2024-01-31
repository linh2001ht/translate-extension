# myapp/serializers.py
from rest_framework import serializers
from .models import Dict

class DictSerializer(serializers.ModelSerializer):
    class Meta:
        model = Dict
        fields = '__all__'
