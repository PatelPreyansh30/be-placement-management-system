from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyView

router = DefaultRouter()
router.register('', CompanyView)

urlpatterns = [
] + router.urls
