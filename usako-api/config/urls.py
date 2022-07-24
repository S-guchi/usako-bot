from django.urls import path, include

urlpatterns = [
    path("account/", include("accounts.urls")),
    path("chat/", include("chat.urls")),
]
