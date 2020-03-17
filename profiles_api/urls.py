from django.urls import path
from .views import (
    HelloApiView,
    )

urlpatterns = [
    path('hello-view/', HelloApiView.as_view())
]
