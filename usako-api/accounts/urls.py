from django.urls import path
from .views import CrudAccount, CrudSpace

urlpatterns = [
    path("v1/account", CrudAccount.as_view()),
    path("v1/space", CrudSpace.as_view()),
]
