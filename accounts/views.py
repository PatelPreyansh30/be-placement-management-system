from rest_framework.generics import CreateAPIView
from rest_framework.viewsets import ModelViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import CustomUserModel
from .serializer import UserSerializer, CustomTokenObtainPairSerializer, CustomTokenRefreshSerializer


class CustomUserSignupView(ModelViewSet):
    queryset = CustomUserModel.objects.all()
    serializer_class = UserSerializer


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = CustomTokenRefreshSerializer
