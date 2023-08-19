from rest_framework.serializers import ModelSerializer
from .models import StudentPersonalDetailModel, StudentCollegeDetailModel, StudentSchoolDetailModel


class StudentPersonalDetailSerializer(ModelSerializer):
    class Meta:
        model = StudentPersonalDetailModel
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
        model = StudentCollegeDetailModel
        fields = '__all__'


class StudentSchoolDetailSerializer(ModelSerializer):
    class Meta:
        model = StudentSchoolDetailModel
        fields = '__all__'
