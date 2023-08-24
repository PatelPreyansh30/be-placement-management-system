from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer, TokenRefreshSerializer
from .models import CustomUserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUserModel
        fields = '__all__'
        extra_kwargs = {
            'firstName': {
                'error_messages': {
                    'blank': "First name is required",
                }
            },
            'lastName': {
                'error_messages': {
                    'blank': "Last name is required",
                }
            },
            'mobile': {
                'error_messages': {
                    'blank': "Mobile is required",
                },
                'validators': [
                    UniqueValidator(
                        queryset=CustomUserModel.objects.all(),
                        message="Mobile number already exists"
                    )
                ]
            },
            'email': {
                'error_messages': {
                    'blank': "Email is required",
                    'invalid': "Enter valid email address",
                },
                'validators': [
                    UniqueValidator(
                        queryset=CustomUserModel.objects.all(),
                        message="Email already exists"
                    )
                ]
            },
            'password': {
                'error_messages': {
                    'blank': "Password is required",
                }
            },
        }

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
    refresh = serializers.CharField(
        error_messages={'blank': "Refresh token is required"})

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
