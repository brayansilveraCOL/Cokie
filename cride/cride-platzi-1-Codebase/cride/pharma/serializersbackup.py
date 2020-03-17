from rest_framework import serializers
from cride.pharma.models import Circle
from rest_framework.validators import UniqueValidator


class CircleSerializer(serializers.Serializer):
    name = serializers.CharField()
    slug_name = serializers.SlugField()
    rides_taken = serializers.IntegerField()
    rides_offered = serializers.IntegerField()
    members_limit = serializers.IntegerField()

class CreateCircleSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=140)
    slug_name = serializers.SlugField(
        max_length=40,
        validators=[
            UniqueValidator(queryset=Circle.objects.all())
        ]## Se utiliza para que la validacion no llegue a BD
    )
    about = serializers.CharField(max_length=255, required=False)

    def create(self, data):
        return Circle.objects.create(**data)

