from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import PlacementApplicationModel


class PlacementApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlacementApplicationModel
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=PlacementApplicationModel.objects.all(),
                fields=['studentId', 'companyId']
            )
        ]