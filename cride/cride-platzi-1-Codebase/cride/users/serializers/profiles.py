#Serializador del perfil de usuarios Clase 36
from rest_framework import serializers

from cride.users.models import Profile

class ProfileModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Profile
        fields = [
            'picture',
            'biography',
            'reputation',
            'rides_offered'
        ]
        ready_only_fields = [
             'biography',
            'reputation'
        ]