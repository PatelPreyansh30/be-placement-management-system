from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from .models import CustomUserModel


class UserSerializer(serializers.ModelSerializer):
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


class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = ['id', 'firstName', 'lastName', 'mobile',
                  'email', 'isStudent', 'isStaff', 'updatedAt']


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        custom_user = self.user
        data['user'] = CustomUserSerializer(custom_user).data
        return data


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        refresh = self.token_class(attrs['refresh'])
        access_token = refresh.access_token
        user_id = access_token.payload.get('user_id')
        user = CustomUserModel.objects.filter(id=user_id).first()

        data = {
            'refresh': str(refresh),
            'access': str(access_token),
            'user': CustomUserSerializer(user).data,
        }

        return data
