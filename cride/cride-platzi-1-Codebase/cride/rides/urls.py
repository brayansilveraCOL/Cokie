
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import rides as ride_views



router = DefaultRouter()
router.register(
    r'circles/(?P<slug_name>[-a-zA-Z0-0_]+)/rides',
    ride_views.RideViewSet,
    basename='ride'
)
urlpatterns = [
    path('', include(router.urls))
]








# para utilizar estas urls se debe activar los archivos backup
#from cride.pharma.views import list_circles, create_circles
#urlpatterns = [
#    path('circles/', list_circles),
#    path('circles/create/', create_circles)   
#]