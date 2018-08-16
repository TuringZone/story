from django.shortcuts import render
from rest_framework import viewsets, generics, permissions
from rest_framework.response import Response
from .models import Story
from .serializers import StorySerializer
# Create your views here.

class StoryViewset(viewsets.ModelViewSet):
    permission_classes = [permissions.IsAuthenticated,]
    serializer_class = StorySerializer
    queryset = Story.objects.all()
