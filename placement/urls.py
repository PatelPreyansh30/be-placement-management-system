from rest_framework.routers import DefaultRouter
from .views import PlacementApplicationView,ApplicationTrackingView

router = DefaultRouter()
router.register('apply', PlacementApplicationView, basename='placement-apply')
router.register('application', ApplicationTrackingView,
                basename='placement-application')

urlpatterns = [
    
] + router.urls
