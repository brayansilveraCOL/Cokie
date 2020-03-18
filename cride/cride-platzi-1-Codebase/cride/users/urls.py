from django.urls import path, include
"""
from cride.users.views.users import UserLoginAPIView
from cride.users.views.users import UserSignUpAPIView
from cride.users.views.users import AccountVerificationAPIView
"""
from cride.users.views import users as user_views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', user_views.UserViewSet, basename='users')
urlpatterns = [
    path('', include(router.urls))
]

