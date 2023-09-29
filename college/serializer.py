from rest_framework.serializers import ModelSerializer
from . import models


class CollegeSerializer(ModelSerializer):
    class Meta:
        model = models.CollegeModel
        fields = ['id', 'label', 'value']


class BranchSerializer(ModelSerializer):
    class Meta:
        model = models.BranchModel
        fields = ['id', 'label', 'value']
