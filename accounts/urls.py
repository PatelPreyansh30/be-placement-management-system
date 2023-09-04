from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('user/post', views.CustomUserPostView, basename='user-post')
router.register('user/update', views.CustomUserUpdateDeleteView,
                basename='user-update')

urlpatterns = [
    path('user/token/', views.CustomTokenObtainPairView.as_view()),
    path('user/token/refresh/', views.CustomTokenRefreshView.as_view()),
] + router.urls
