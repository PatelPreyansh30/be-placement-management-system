from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentRegistrationView, CustomTokenObtainPairView

router = DefaultRouter()

urlpatterns = [
    path('student/register/', StudentRegistrationView.as_view()),
    path('student/token/', CustomTokenObtainPairView.as_view()),
] + router.urls
