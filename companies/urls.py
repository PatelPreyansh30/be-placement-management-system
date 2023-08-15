from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyView, CompanyDetailView, CompanyDocumentView

router = DefaultRouter()
router.register('basic', CompanyView)
router.register('document', CompanyDocumentView)
router.register('detail', CompanyDetailView, basename='detail')

urlpatterns = [
] + router.urls
