from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('personal', views.FacultyPersonalView)
router.register('dashboard-profile',
                views.FacultyDashboardView, basename='faculty-dashboard-profile')

urlpatterns = [
] + router.urls
