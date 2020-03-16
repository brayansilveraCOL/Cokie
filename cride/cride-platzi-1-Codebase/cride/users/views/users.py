#Users Views
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from cride.users.serializers.users import UserLoginSerializer, UserModelSerializer, UserSignupSerializer
class UserLoginAPIView(APIView):


    def post(self, request, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)


class UserSignUpAPIView(APIView):


    def post(self, request, *args, **kwargs):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data,
       
        return Response(data, status=status.HTTP_201_CREATED)
