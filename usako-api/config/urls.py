from django.urls import path, include

urlpatterns = [
    path("account/v1/", include("accounts.urls")),
    path("chat/", include("chat.urls")),
]
