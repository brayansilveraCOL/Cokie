
from django.urls import include, path

from rest_framework.routers import DefaultRouter
from cride.pharma.views import circles as circle_views
router = DefaultRouter()
router.register(r'circles', circle_views.CircleViewSet, basename='circle')

urlpatterns = [
    path('', include(router.urls))
]








# para utilizar estas urls se debe activar los archivos backup
#from cride.pharma.views import list_circles, create_circles
#urlpatterns = [
#    path('circles/', list_circles),
#    path('circles/create/', create_circles)   
#]