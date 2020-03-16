from django.db import models
from cride.utils.models import UtilsModel



class Circle(UtilsModel):
    name = models.CharField('cicle name', max_length=140)
    slug_name = models.SlugField(unique=True, max_length=40)
    about = models.CharField('circle description', max_length=255)
    picture = models.ImageField(upload_to='pharma/pictures', blank=True, null=True)
    rides_offered = models.PositiveIntegerField(default=0)
    rides_taken = models.PositiveIntegerField(default=0)
    verified = models.BooleanField(
        'verified circle',
        default=False,
        help_text='Verified circles are also known as official communities.'
    )
    is_public = models.BooleanField(
        default = True,
        help_text ='Public Cicrcles are listed in the main page so everyone know about their existence.'
    )
    is_limited = models.BooleanField(
        'limited',
        default=False,
        help_text='Limited circles can grow up to a fixed number of members'
    )
    members_limit = models.PositiveIntegerField(
        default=0,
        help_text='If circle is limited, this willl be the limit on the number of members'
    )

    def __str__(self):
        return self.name

    class Meta(UtilsModel.Meta):
        ordering = ['-rides_taken', '-rides_offered']