from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CompanyView, CompanyDetailView, CompanyDocumentView, OpenCompanyView, ClosedCompanyView

router = DefaultRouter()
router.register('basic', CompanyView)
router.register('document', CompanyDocumentView)
router.register('detail', CompanyDetailView, basename='detail')
router.register('open', OpenCompanyView, basename='open')
router.register('closed', ClosedCompanyView, basename='closed')

urlpatterns = [
] + router.urls
