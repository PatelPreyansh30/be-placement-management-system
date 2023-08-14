from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView
from .models import CustomUserModel
from .serializer import CustomUserSerializer, CustomTokenObtainPairSerializer


class CustomUserSignupView(ModelViewSet):
    queryset = CustomUserModel.objects.all()
    serializer_class = CustomUserSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer
