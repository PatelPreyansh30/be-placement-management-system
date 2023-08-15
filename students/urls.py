from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentPersonalDetailView, StudentCollegeDetailView, StudentSchoolDetailView

router = DefaultRouter()
router.register('personal', StudentPersonalDetailView)
router.register('college', StudentCollegeDetailView)
router.register('school', StudentSchoolDetailView)

urlpatterns = [
] + router.urls
