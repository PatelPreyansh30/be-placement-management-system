from rest_framework import serializers
from .models import PlacementApplicationModel


class PlacementApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacementApplicationModel
        fields = '__all__'