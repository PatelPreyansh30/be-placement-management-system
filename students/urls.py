from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentPersonalDetailView

router = DefaultRouter()
router.register('personal', StudentPersonalDetailView)

urlpatterns = [
] + router.urls