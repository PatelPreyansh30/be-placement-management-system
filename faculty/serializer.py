from rest_framework.serializers import ModelSerializer
from .models import FacultyPersonalModel


class FacultyPersonalSerializer(ModelSerializer):
    class Meta:
        model = FacultyPersonalModel
        fields = '__all__'

    def update(self, instance, validated_data):
        new_profile_pic = validated_data.get('profilePic')

        if new_profile_pic:
            instance.profilePic.delete()
            instance.profilePic = new_profile_pic
        
        instance.save()
        return instance
