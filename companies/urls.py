from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyView, CompanyDetailView, CompanyDocumentView

router = DefaultRouter()
router.register('create', CompanyView, basename='company-post-put-delete')
router.register('document', CompanyDocumentView,
                basename='company-document-post-put-delete')
router.register('details', CompanyDetailView, basename='company-get')

urlpatterns = [
] + router.urls
