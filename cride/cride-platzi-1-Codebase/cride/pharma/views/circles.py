"""Cicless views."""

from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from cride.pharma.models import Circle, Membership
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from cride.pharma.serializers.circles import CircleModelSerializer
from cride.pharma.permissions.circles import IsCircleAdmin

class CircleViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    viewsets.GenericViewSet,
                    mixins.UpdateModelMixin):
    ##queryset = Circle.objects.all() listar sin condicion
    serializer_class = CircleModelSerializer    
    lookup_field = 'slug_name' #se utiliza para buscar por param en url
    #Filters
    filter_backends = (SearchFilter, OrderingFilter, DjangoFilterBackend)
    ordering_fields = ('rides_offered', 'rides_taken', 'name', 'created', 'member_limit')
    ordering = ('-rides_offered', '-rides_taken')#'members__count',  Bug
    filter_fields = ('verified', 'is_limited')
    def get_queryset(self):
        ## listar con parametros de busqueda
        queryset =  Circle.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        return queryset
    def get_permissions(self):
        #Assign permissions based on action
        permissions = [IsAuthenticated]
        if self.action in ['update', 'partial_update']:
            permissions.append(IsCircleAdmin)
        return [permission() for permission in permissions]

    
    def perform_create(self, serializer):
        #Asignar Administrador al circulo
        circle = serializer.save()
        user = self.request.user
        profile = user.profile
        Membership.objects.create(
            user=user,
            profile=profile,
            circle=circle,
            is_admin=True,
            remaining_invitations=10
        )
    