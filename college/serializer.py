from rest_framework.serializers import ModelSerializer
from . import models


class CollegeSerializer(ModelSerializer):
    class Meta:
        model = models.CollegeModel
        fields = ['id', 'name']
        extra_kwargs = {
            'name': {
                'error_messages': {
                    'blank': "College name is required",
                }
            },
        }


class BranchSerializer(ModelSerializer):
    class Meta:
        model = models.BranchModel
        fields = ['id', 'name']
        extra_kwargs = {
            'name': {
                'error_messages': {
                    'blank': "Branch name is required",
                }
            },
        }
