#Users Views
from rest_framework.views import APIView
from rest_framework.decorators  import action
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from cride.users.permissions import IsAccountOwner
from cride.users.serializers.users import UserLoginSerializer, UserModelSerializer, UserSignupSerializer, AccountVerificationSerializer
from cride.users.serializers.profiles import ProfileModelSerializer #Clase 36
from cride.users.models import User
from cride.pharma.models import Circle
from cride.pharma.serializers.circles import CircleModelSerializer

class UserViewSet(mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet,
                    mixins.UpdateModelMixin):#Clae 35 y 36
    #Handle Sign in, Login and account verification
    queryset = User.objects.filter(is_active=True, is_client=True)#Cambios clase 35
    serializer_class = UserModelSerializer#Cambios clase 35
    lookup_field = 'username'#Cambios clase 35
    #Cambios clase 35
    def get_permissions(self):#Cambios clase 35
        #Assign permissions based on action
        if self.action in ['signup', 'login', 'verify']:#Cambios clase 35
            permissions = [AllowAny]#Cambios clase 35
        elif self.action == ['retrieve', 'update', 'partial__update']:#Cambios clase 35 y 36
            permissions = [IsAuthenticated, IsAccountOwner]#Cambios clase 35
        else:#Cambios clase 35
            permissions = [IsAuthenticated]#Cambios clase 35
        return [p() for p in permissions]#Cambios clase 35

    @action(detail=False, methods=['post'])
    def login(self, request):
        #User sign in
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user, token = serializer.save()
        data = {
            'user': UserModelSerializer(user).data,
            'access_token': token
        }
        return Response(data, status=status.HTTP_201_CREATED)

    @action(detail=False, methods=['post'])
    def signup(self, request):
        #User sign up
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data,
        return Response(data, status=status.HTTP_201_CREATED)
    
    @action(detail=False, methods=['post'])
    def verify(self, request):
        #Verify Account
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Bienvenido Cuenta verificada'}
        return Response(data, status=status.HTTP_200_OK)
    @action(detail=True, methods=['put', 'patch'])#item clase #36
    def profile(self, request, *args, **kwargs):#item clase #36
        #clase 36 agregamos el mixin de update de usuarios
        # se actualizaron los permisos en el self.action retrive
        #Agregamos el def profile para el update de usuarios
        #Lo hicimos a partir de un Model Serializer no se creo un nuevo serializer
        user = self.get_object()#item clase #36
        profile = user.profile#item clase #36
        partial = request.method == 'PATCH'#item clase #36
        serializer = ProfileModelSerializer(#item clase #36
            profile,#item clase #36
            data=request.data,#item clase #36
            partial=partial#item clase #36
        )#item clase #36
        serializer.is_valid(raise_exception=True)#item clase #36
        serializer.save()#item clase #36
        data = UserModelSerializer(user).data#item clase #36
        return Response(data)#item clase #36
    def retrieve(self, request, *args, **kwargs):#Cambios clase 35
        #Add extra data to the response
        
        response = super(UserViewSet, self).retrieve(request, *args, **kwargs)#Cambios clase 35
        circles = Circle.objects.filter(#Cambios clase 35
            members=request.user,
            membership__is_active=True
        )
        data = {#Cambios clase 35 ###Bug Salen los circulos de la persona logueada al consultar otra persona desinta
            'user': response.data,
            'circles': CircleModelSerializer(circles, many=True).data
        }
        response.data = data#Cambios clase 35
      
        return response#Cambios clase 35

"""
Esto puede utilizarse Sirve.!
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
"""

"""
class UserSignUpAPIView(APIView):


    def post(self, request, *args, **kwargs):
        serializer = UserSignupSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        data = UserModelSerializer(user).data,
       
        return Response(data, status=status.HTTP_201_CREATED)
"""
"""
class AccountVerificationAPIView(APIView):

    def post(self, request, *args, **kwargs):
        serializer = AccountVerificationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        data = {'message': 'Bienvenido Cuenta verificada'}
        return Response(data, status=status.HTTP_200_OK)
"""