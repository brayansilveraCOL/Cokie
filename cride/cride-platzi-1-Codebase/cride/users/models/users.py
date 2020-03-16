from django.db import models
from django.contrib.auth.models import AbstractUser

from cride.utils.models import UtilsModel
from django.core.validators import RegexValidator
class User(UtilsModel, AbstractUser):
    email = models.EmailField(
        'Email address',
        unique=True,
        error_messages={
            'unique':'A user with that email already exists.'
        }
       
    )


    phone_regex = RegexValidator(
        regex=r'\+?1?\d{9,15}$',
        message="No admitido"
    )
    phone = models.CharField(
        validators=[phone_regex],
        max_length =17,
        blank=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'phone']
    is_client = models.BooleanField(
        'CLIENT STATUS',
        default=True,
        help_text=(
            'Clients are the main type of user.'
        )
    )
    is_verified = models.BooleanField(
        'verified',
        default=True,
        help_text='set to true when the user have verified its email address',
    )
    
    def __str__(self):
        return self.username
    
    def get_short_name(self):
        return self.username