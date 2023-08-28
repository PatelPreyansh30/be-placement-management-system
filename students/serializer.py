from rest_framework.serializers import ModelSerializer
from django.contrib.auth import get_user_model
from . import models

User = get_user_model()


class StudentPersonalDetailSerializer(ModelSerializer):
    class Meta:
        model = models.StudentPersonalDetailModel
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


class StudentCollegeDetailSerializer(ModelSerializer):
    class Meta:
        model = models.StudentCollegeDetailModel
        fields = '__all__'


class StudentSchoolDetailSerializer(ModelSerializer):
    class Meta:
        model = models.StudentSchoolDetailModel
        fields = '__all__'


class StudentDetailedSerializer(ModelSerializer):
    college_detail = StudentCollegeDetailSerializer(read_only=True)
    school_detail = StudentSchoolDetailSerializer(read_only=True)

    class Meta:
        model = models.StudentPersonalDetailModel
        fields = '__all__'


class StudentProfilPicForDashboardSerializer(ModelSerializer):
    class Meta:
        model = models.StudentPersonalDetailModel
        fields = ['profilePic']


class StudentForDashboardSerializer(ModelSerializer):
    studentDetail = StudentProfilPicForDashboardSerializer(read_only=True)

    class Meta:
        model = User
        fields = ['id', 'firstName', 'lastName', 'studentDetail']
