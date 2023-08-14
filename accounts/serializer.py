from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import CustomUserModel


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = '__all__'

    def create(self, validate_data):
        try:
            password = validate_data.pop('password')
            user = CustomUserModel.objects.create_user(
                email=validate_data.pop('email'), password=password, **validate_data)
            return user
        except:
            raise serializers.ValidationError(
                {'password': ['This field may not be blank.']})


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        custom_user = self.user
        data['user'] = CustomUserSerializer(custom_user).data
        return data
