from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CustomUserSignupView, CustomTokenObtainPairView, CustomTokenRefreshView

router = DefaultRouter()

urlpatterns = [
    path('user/signup/', CustomUserSignupView.as_view({'post': 'create'})),
    path('user/token/', CustomTokenObtainPairView.as_view()),
    path('user/token/refresh/', CustomTokenRefreshView.as_view()),
] + router.urls
