from rest_framework.serializers import ModelSerializer
from .models import StudentPersonalDetailModel


class StudentPersonalDetailSerializer(ModelSerializer):
    class Meta:
        model = StudentPersonalDetailModel
        fields = '__all__'

    def update(self, instance, validated_data):
        new_resume = validated_data.get('resume')
        new_profile_pic = validated_data.get('profilePic')
        if new_resume:
            instance.resume.delete()
            instance.resume = new_resume
        if new_profile_pic:
            instance.profilePic.delete()
            instance.profilePic = new_profile_pic
        instance.save()
        return instance
