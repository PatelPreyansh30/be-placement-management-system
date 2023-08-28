from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class StudentSerializer(ModelSerializer):
    class Meta:
        model = models.StudentModel
        fields = '__all__'

    def update(self, instance, validated_data):
        new_resume = validated_data.get('resume')
        new_profile_pic = validated_data.get('profilePic')
        new_guideline_form = validated_data.get('placementGuidelineForm')
        if new_resume:
            instance.resume.delete()
            instance.resume = new_resume
        if new_profile_pic:
            instance.profilePic.delete()
            instance.profilePic = new_profile_pic
        if new_guideline_form:
            instance.placementGuidelineForm.delete()
            instance.placementGuidelineForm = new_guideline_form
        instance.save()
        return instance


class StudentDetailedSerializer(ModelSerializer):
    studentDetail = StudentSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'studentDetail',
                  'mobile', 'email', 'isStudent', 'isStaff']
