from rest_framework import viewsets, mixins, permissions
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import serializer, models


class CustomUserPostView(mixins.CreateModelMixin, viewsets.GenericViewSet):
    queryset = models.CustomUserModel.objects.all()
    serializer_class = serializer.UserSerializer


class CustomUserUpdateDeleteView(mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    queryset = models.CustomUserModel.objects.all()
    serializer_class = serializer.UserSerializer
    # permission_classes = [permissions.IsAuthenticated]


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = serializer.CustomTokenObtainPairSerializer


class CustomTokenRefreshView(TokenRefreshView):
    serializer_class = serializer.CustomTokenRefreshSerializer
