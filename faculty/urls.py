from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('create', views.FacultyCreateView, basename='faculty-create')
router.register('profile',
                views.FacultyDetailedView, basename='faculty-profile')

urlpatterns = [
] + router.urls
