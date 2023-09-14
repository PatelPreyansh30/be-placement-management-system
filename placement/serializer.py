from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import PlacementApplicationModel
from companies.serializer import CompanySerializer

class PlacementApplicationSerializer(serializers.ModelSerializer):
    companyId = CompanySerializer(read_only=True)
    class Meta:
        model = PlacementApplicationModel
        fields = '__all__'
        validators = [
            UniqueTogetherValidator(
                queryset=PlacementApplicationModel.objects.all(),
                fields=['studentId', 'companyId']
            )
        ]