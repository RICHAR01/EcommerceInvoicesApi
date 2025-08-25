from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny
from users.api.serializers import UserSerializer

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from users.api.serializers import UserRegisterSerializer, UserSerializer, UserUpdateSerializer
from users.models import User


# class UserRegistrationView(CreateAPIView):
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]


class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegisterSerializer(data=request.data)

        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
