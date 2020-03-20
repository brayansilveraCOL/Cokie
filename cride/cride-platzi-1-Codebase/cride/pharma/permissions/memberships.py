#Circles permission CLasess
from rest_framework.permissions import BasePermission
from cride.pharma.models import Membership
class IsActiveCircleMember(BasePermission):
    """Allow access only to circle members
       Expect that the views implemnting this permission
       have a circle atribute assigne
    """
    def has_permission(self, request, view):
        try:
            Membership.objects.get(
                user=request.user,
                circle=view.circle,
                is_active=True
            )
        except Membership.DoesNotExist:
            return False
        return True
class IsAdminOrMembershipOwner(BasePermission):
    """
    Allow accese only to (Circle's admin) or users
    that are owner of the membership (object).
    """

    def has_permission(self, request, view):
        membership = view.get_object()
        if membership.user == request.user:
            return True

        try:
            Membership.objects.get(
                circle=view.circle,
                user=request.user,
                is_active=True,
                is_admin=True
            )
        except Membership.DoesNotExist:
            return False
        return True
class IsSelfMember(BasePermission):
    """Allow access only to member owners"""
    def has_permission(self, request, view):
        """Let object permission grant access"""
        obj = view.get_object()
        return self.has_object_permission(request, view, obj)
    
    def has_object_permission(self, request, view, obj):
        """Allow access only if member is owned by the requesting user"""
        return request.user==obj.user
