from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import CustomUserSignupView, CustomTokenObtainPairView

router = DefaultRouter()

urlpatterns = [
    path('user/signup/', CustomUserSignupView.as_view({'post': 'create'})),
    path('user/token/', CustomTokenObtainPairView.as_view()),
    path('user/token/refresh/', TokenRefreshView.as_view()),
] + router.urls
