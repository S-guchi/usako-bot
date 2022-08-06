from django.urls import path
from .views import CrudUser, CrudSpace

urlpatterns = [
    path("v1/user", CrudUser.as_view()),
    path("v1/space", CrudSpace.as_view()),
]
