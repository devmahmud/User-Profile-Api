from django.urls import path
from django.urls import include
from rest_framework.routers import DefaultRouter

from .views import (
    HelloApiView,
    HelloViewset
    )

router = DefaultRouter()
router.register('hello-viewset', HelloViewset, basename='hello-viewset')

urlpatterns = [
    path('hello-view/', HelloApiView.as_view()),
    path('', include(router.urls)),
]
