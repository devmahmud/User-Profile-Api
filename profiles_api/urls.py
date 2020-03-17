from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import (
    HelloApiView,
    HelloViewSet,
    UserProfileViewSet
    )

router = DefaultRouter()
router.register('hello-viewset', HelloViewSet, basename='hello-viewset')
router.register('profile', UserProfileViewSet, basename="profile" )

urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('', include(router.urls)),
]
