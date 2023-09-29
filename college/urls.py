from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('college', views.CollegeViewSet, basename='college-types')
router.register('branch', views.BranchViewSet, basename='branch-types')

urlpatterns = [
] + router.urls
