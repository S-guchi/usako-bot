from django.shortcuts import render
from rest_framework.generics import ListAPIView

# Create your views here.


class chatV1(ListAPIView):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
