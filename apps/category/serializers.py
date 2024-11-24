from rest_framework import serializers
from .models import *

#Esto converte el modelo a un json
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=[
            'id',
            'name',
            'slug',
            'views'
        ]