from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyView, CompanyDetailView, CompanyDocumentView

router = DefaultRouter()
router.register('create', CompanyView, basename='company-create')
router.register('document/create', CompanyDocumentView,
                basename='company-document-create')
router.register('profile', CompanyDetailView, basename='company-profile')

urlpatterns = [
] + router.urls
