from django.urls import path
from cride.users.views.users import UserLoginAPIView
from cride.users.views.users import UserSignUpAPIView
from cride.users.views.users import AccountVerificationAPIView
urlpatterns = [
    path('users/login/', UserLoginAPIView.as_view(), name='login'),
    path('users/signup/', UserSignUpAPIView.as_view(), name='signup'),
    path('users/verify/', AccountVerificationAPIView.as_view(), name='verify'),
]
