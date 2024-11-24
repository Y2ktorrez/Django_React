from rest_framework import serializers
from .models import *

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'slug',
            'thumbnail',
            'excerpt',
            'description',
            'published',
            'time_read',
            'views',
            'category'
        ]