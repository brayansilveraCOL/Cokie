from rest_framework.permissions import BasePermission

#Cambios Clase 35
class IsAccountOwner(BasePermission):

    def has_object_permission(self, request, view, obj):

        return request.user == obj