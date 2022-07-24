from django.urls import path
from .views import chatV1

urlpatterns = [
    path("v1", chatV1.as_view()),
]
