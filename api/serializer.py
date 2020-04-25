from rest_framework import serializers
from .models import articles

class ArticlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = articles
        fields = ['pk','description','status','price','image']