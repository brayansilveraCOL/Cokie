from django.urls import path
from cride.users.views.users import UserLoginAPIView
from cride.users.views.users import UserSignUpAPIView
urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/signup/', UserSignUpAPIView.as_view(), name='signup'),
]
