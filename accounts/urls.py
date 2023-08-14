from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView
from .views import StudentRegistrationView, CustomTokenObtainPairView

router = DefaultRouter()

urlpatterns = [
    path('student/register/', StudentRegistrationView.as_view({'post': 'create'})),
    path('student/token/', CustomTokenObtainPairView.as_view()),
    path('student/token/refresh/', TokenRefreshView.as_view()),
] + router.urls
