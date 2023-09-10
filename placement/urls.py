from rest_framework.routers import DefaultRouter
from .views import PlacementApplicationView

router = DefaultRouter()
router.register('apply', PlacementApplicationView)

urlpatterns = [
    
] + router.urls
