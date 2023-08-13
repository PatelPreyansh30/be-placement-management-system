from rest_framework import serializers
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from .models import StudentModel


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentModel
        fields = ("id", "firstName", "lastName", "mobile", "whatsappMobile",
                  "alternateMobile", "email", "address", "city", "isVerified", "isBlocked",)

    def create(self, validate_data):
        password = validate_data.pop('password')
        student = StudentModel.objects.create_user(
            email=validate_data.pop('email'), password=password, **validate_data)
        return student


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        student = self.user
        data['user'] = StudentSerializer(student).data
        return data
