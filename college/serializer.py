from rest_framework.serializers import ModelSerializer
from . import models


class CollegeSerializer(ModelSerializer):
    class Meta:
        model = models.CollegeModel
        fields = ['id', 'label', 'value']
