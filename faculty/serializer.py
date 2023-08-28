from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class FacultySerializer(ModelSerializer):
    class Meta:
        model = models.FacultyModel
        fields = '__all__'

    def update(self, instance, validated_data):
        new_profile_pic = validated_data.get('profilePic')

        if new_profile_pic:
            instance.profilePic.delete()
            instance.profilePic = new_profile_pic

        instance.save()
        return instance


class FacultyDetailedSerializer(ModelSerializer):
    facultyDetail = FacultySerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'facultyDetail',
                  'mobile', 'email', 'isStudent', 'isStaff']
