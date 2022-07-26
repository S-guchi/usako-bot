from django.urls import path
from .views import CrudAccount

urlpatterns = [
    path("v1/", CrudAccount.as_view()),
]
