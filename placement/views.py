from django.shortcuts import render
from rest_framework import mixins, viewsets, permissions
from . import models,serializer

# Create your views here.
class PlacementApplicationView(viewsets.ModelViewSet):
    queryset = models.PlacementApplicationModel.objects.all()
    serializer_class = serializer.PlacementApplicationSerializer
    
    # permission_classes = [permissions.IsAuthenticated]