from django.db import models

from cride.utils.models import UtilsModel
from .users import User

class Profile(UtilsModel):
    user = models.OneToOneField('users.User', on_delete=models.CASCADE)
    picture = models.ImageField(
        'profile picture',
        upload_to='users/pictures/',
        blank=True, null=True
    )
    biography = models.TextField(max_length=500, blank=True)
    buy_sum = models.PositiveIntegerField(default=0)
    reputation = models.FloatField(
        default=5.0,
        help_text="Users Reputation"
    )
    def __str__(self):
        return str(self.user)