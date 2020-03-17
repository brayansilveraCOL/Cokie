from cride.pharma.models import Circle
from rest_framework.decorators import api_view
from rest_framework.response import Response

# from cride.pharma.serializers import CircleSerializer, CreateCircleSerializer
@api_view(['GET'])
def list_circles(request):
    circles = Circle.objects.all()
    public = circles.filter(is_public=True)
    #Serializer query set public 
    # serializer = CircleSerializer(circles, many=True)
    data = []
    for circle in public:
        data.append({
            'name': circle.name,
            'slug_name': circle.slug_name,
            'rides_taken': circle.rides_taken,
            'rides_offered': circle.rides_offered,
            'members_limit': circle.members_limit,
            #serializer = CircleSerializer(circle)
            #data.append(serializers.data)
        })
    return Response(data)
    #return Response(serializer.data) ---- >>> queryset Serialziado
@api_view(['POST'])
def create_circles(request):
    #Crear Serializar
    #serializer = CreateCircleSerializer(data=request.data)(1)
    #serializer.is_valid(raise_exception=True)(2)
    #data = serializer.data(3)
    #circle = Circle.objects.create(**data)(4)
    #Con la actualizacion de def create se onmite las lineas 3 y 4 y se remplaza por
    #circle = serializer.save()
    name = request.data['name']
    slug_name = request.data['slug_name']
    about = request.data.get('about', '')
    circle = Circle.objects.create(name=name, slug_name=slug_name, about=about)
    data = {
        'name': circle.name,
            'slug_name': circle.slug_name,
            'rides_taken': circle.rides_taken,
            'rides_offered': circle.rides_offered,
            'members_limit': circle.members_limit,
    }
    return Response(data)
    #return crear serializer
    #return Response(CircleSerializer(circle).data)

