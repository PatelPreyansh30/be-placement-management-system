from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentRegistrationView

router = DefaultRouter()

urlpatterns = [
    path('student/register/', StudentRegistrationView.as_view()), 
] + router.urls