from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FacultyPersonalView

router = DefaultRouter()
router.register('personal', FacultyPersonalView)

urlpatterns = [
] + router.urls
