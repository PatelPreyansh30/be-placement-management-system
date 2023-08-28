from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('detail', views.StudentView, basename='student-detail')
router.register('profile', views.StudentDetailedView,
                basename='student-profile')

urlpatterns = [
] + router.urls
