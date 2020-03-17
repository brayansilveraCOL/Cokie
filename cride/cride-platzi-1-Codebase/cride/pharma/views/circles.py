"""Cicless views."""

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from cride.pharma.models import Circle

from cride.pharma.serializers.circles import CircleModelSerializer



class CircleViewSet(viewsets.ModelViewSet):
    ##queryset = Circle.objects.all() listar sin condicion
    serializer_class = CircleModelSerializer
    permission_classes = (IsAuthenticated,)
    


    def get_queryset(self):
        ## listar con parametros de busqueda
        queryset =  Circle.objects.all()
        if self.action == 'list':
            return queryset.filter(is_public=True)
        return queryset
    