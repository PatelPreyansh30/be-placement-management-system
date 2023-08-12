from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentProfileView

router = DefaultRouter()
router.register(r'student', StudentProfileView, basename='student')

urlpatterns = [
] + router.urls