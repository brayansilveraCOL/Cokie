
from django.urls import path
from cride.pharma.views import list_circles, create_circles
urlpatterns = [
    path('circles/', list_circles),
    path('circles/create/', create_circles)
    
]
