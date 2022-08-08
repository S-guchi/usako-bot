from django.urls import path
from .views import CrudUser, CrudSpace, LinkAccountSpace

urlpatterns = [
    path("user", CrudUser.as_view()),
    path("space", CrudSpace.as_view()),
    path("linkspace", LinkAccountSpace.as_view()),
]
