from django.shortcuts import get_object_or_404
from rest_framework import status, exceptions
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from django.db import transaction
import traceback
from .models import Space, User
from .serializers import UserSerializer


class CrudAccount(RetrieveUpdateDestroyAPIView):
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
                status=status.HTTP_201_CREATED,
            )
        except User.DoesNotExist:
            return Response(
                data={"error-message": "ユーザーが見つかりませんでした。"},
                status=status.HTTP_404_NOT_FOUND,
            )

        except Exception:
            print(traceback.format_exc())
            return Response(
                data={"error-message": "不明なエラーが発生しました。"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def put(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            serializer.save()
            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )
        except exceptions.ValidationError as e:
            print(traceback.format_exc())
            return Response(
                data={"error-message": e.detail},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

            # return Response()
        except Exception:
            print(traceback.format_exc())
            return Response(
                data={"error-message": "不明なエラーが発生しました。"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def patch(self, request, *args, **kwargs):
        # https://qiita.com/aja_min/items/a84b00c74225e41e7da5
        try:

            user = get_object_or_404(User, line_id=request.data["line_id"])

            serializer = self.get_serializer(
                instance=user, data=request.data, partial=True
            )
            serializer.is_valid(raise_exception=True)

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_200_OK,
            )

        except Exception:
            print(traceback.format_exc())
            return Response(
                data={"error-message": "不明なエラーが発生しました。"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

    def delete(self, request, *args, **kwargs):
        try:

            user = get_object_or_404(User, line_id=request.query_params["line_id"])

            user.delete()

            return Response(
                status=status.HTTP_200_OK,
            )

        except Exception:
            print(traceback.format_exc())
            return Response(
                data={"error-message": "不明なエラーが発生しました。"},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )
