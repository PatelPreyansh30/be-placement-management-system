from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class FacultyPersonalSerializer(ModelSerializer):
    class Meta:
        model = models.FacultyPersonalModel
        fields = '__all__'

    def update(self, instance, validated_data):
        new_profile_pic = validated_data.get('profilePic')

        if new_profile_pic:
            instance.profilePic.delete()
            instance.profilePic = new_profile_pic

        instance.save()
        return instance


class FacultyProfilePicForDashboardSerializer(ModelSerializer):
    class Meta:
        model = models.FacultyPersonalModel
        fields = ['profilePic']


class FacultyDashboardSerializer(ModelSerializer):
    facultyDetail = FacultyProfilePicForDashboardSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'facultyDetail']
