from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer


class UserLoginViewSet(mixins.CreateModelMixin,
                      viewsets.GenericViewSet):

    serializer_class = LoginSerializer
    permission_classes = (AllowAny, )

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)

        try:
            if serializer.is_valid():
                return Response(serializer.validated_data)
            else:
                return Response(data=serializer.errors, status=400)
        except Exception as e:
            return Response(status=400, data=e.args)
