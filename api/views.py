from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics,viewsets
from rest_framework.permissions import IsAdminUser
from .models import articles
from .serializer import ArticlesSerializer

# Create your views here.
class ListArticles(viewsets.ModelViewSet):
	lookup_field = 'pk'
	queryset = articles.objects.all()
	serializer_class = ArticlesSerializer
	#permission_classes = (IsAdminUser,)