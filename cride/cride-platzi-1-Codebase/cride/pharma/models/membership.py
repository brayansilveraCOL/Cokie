from django.db import models
from cride.utils.models import UtilsModel

class Membership(UtilsModel):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    profile = models.ForeignKey("users.Profile", on_delete=models.CASCADE)
    circle = models.ForeignKey("pharma.Circle", on_delete=models.CASCADE)
    is_admin = models.BooleanField(
        'circle admin',
        help_text="Circle admin can update the circls data manage its members"
    )
    #invitaciones
    used_invitations = models.PositiveIntegerField(default=0)
    remaining_invitations = models.PositiveIntegerField(default=0)
    inivited_by = models.ForeignKey(
        "users.User", 
        null=True,
        on_delete=models.SET_NULL,
        related_name = 'invited_by'
    )
    rides_taken = models.PositiveIntegerField(default=0)
    rides_offered = models.PositiveIntegerField(default=0)
    is_active = models.BooleanField(
        'active status',
        default=True,
        help_text= 'Only active users are allowed to interact in the circle'
    )
    def __str__(self):
        return '@{} at #{}'.format(
            self.user.username,
            self.circle.slug_name
        )
    