from django.urls import path
from .views import account

urlpatterns = [
    path("v1", account.as_view()),
]
