from django.db import models


class UtilsModel(models.Model):
    created = models.DateTimeField(
        'Created at',
        auto_now_add = True,
        help_text = 'Date Time on which the object was created.'

    )
    modified = models.DateTimeField(
        'Modified at',
        auto_now=True,
        help_text='Date Time on which the object last Modified'
    )

    class Meta:
        abstract = True,
        get_latest_by = 'created',
        ordering = ['-created', '-modified']