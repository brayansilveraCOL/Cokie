from rest_framework import serializers
from cride.users.serializers.users import UserModelSerializer
from cride.pharma.models import Membership

class MembershipModelSerializer(serializers.ModelSerializer):
    #member model serialzier
    user = UserModelSerializer(read_only=True)
    inivited_by = serializers.StringRelatedField()
    joined_at = serializers.DateTimeField(source='created', read_only=True)
    class Meta:
        #Meta class
        model = Membership
        fields = [
            'user',
            'is_admin',
            'is_active',
            'used_invitations',
            'remaining_invitations',
            'inivited_by',
            'rides_taken',
            'rides_offered',
            'joined_at'
        ]
        read_only_fields = [
            'user',
            'used_invitations',
            'inivited_by',
            'rides_taken',
            'rides_offered',
        ]