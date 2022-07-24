from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.db import transaction

from .models import Space, User
from .serializers import UserSerializer


class account(RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer

    def get(self, request, *args, **kwargs):
        try:

            if "line_id" in request.GET:
                # query_paramが指定されている場合の処理
                line_id = request.GET.get("line_id")
            else:
                return Response(
                    data={"error-message": "line_idが必要です。"},
                    status=status.HTTP_400_BAD_REQUEST,
                )

            user = User.objects.get(line_id=line_id)
            serializer = UserSerializer(user)
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        except Exception:
            return Response(
                data={"error-message": "不明なエラーが発生しました。"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            line_id = request.data["line_id"]
            nickname = request.data["nickname"]
            space = request.data["space"]

            if space is "":
                space = None

            User.objects.create(
                line_id=line_id,
                nickname=nickname,
                space=space,
            )
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        except Exception:
            return Response(
                data={"error-message": "不明なエラーが発生しました。"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
