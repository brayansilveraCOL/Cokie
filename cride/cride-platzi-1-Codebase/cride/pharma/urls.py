
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from cride.pharma.views import circles as circle_views
from cride.pharma.views import memberships as membership_views
router = DefaultRouter()
router.register(r'circles', circle_views.CircleViewSet, basename='circle')
router.register(
    r'circles/(?P<slug_name>[-a-zA-Z0-0_]+)/members',
    membership_views.MembershipViewSet,
    basename='membership'
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