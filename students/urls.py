from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('personal', views.StudentPersonalDetailView)
router.register('college', views.StudentCollegeDetailView)
router.register('school', views.StudentSchoolDetailView)
router.register('detail', views.StudentDetailedViewset, basename='detail')
router.register('dashboard-profile',
                views.StudentForDashboardView, basename='dashboard-profile')

urlpatterns = [
] + router.urls
