from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentPersonalDetailView, StudentCollegeDetailView

router = DefaultRouter()
router.register('personal', StudentPersonalDetailView)
router.register('college', StudentCollegeDetailView)

urlpatterns = [
] + router.urls