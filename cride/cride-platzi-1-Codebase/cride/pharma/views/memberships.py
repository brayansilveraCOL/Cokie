# Circle membership views
from cride.pharma.models import Circle
from rest_framework import mixins, viewsets
from rest_framework.generics import get_object_or_404
from cride.pharma.serializers.memberships import MembershipModelSerializer
from cride.pharma.models.membership import Membership
class MembershipViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    #Circle Member ship view set
    serializer_class = MembershipModelSerializer
    def dispatch(self, request, *args, **kwargs):
        #Verify that the circle exists
        slug_name=kwargs['slug_name']
        self.circle = get_object_or_404(
            Circle,
            slug_name=slug_name
        )
        return super(MembershipViewSet, self).dispatch(request, *args, **kwargs)
    def get_queryset(self):
        #Return circle Members
        return Membership.objects.filter(
            circle=self.circle,
            is_active=True
        )
    
    
