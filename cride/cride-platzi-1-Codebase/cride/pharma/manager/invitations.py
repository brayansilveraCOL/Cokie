#Circle invitation managers
from django.db import models

import random
from string import ascii_uppercase, digits

class InvitiationManager(models.Manager):
    """
    Invitation manager

    Used to handle code creation
    """
    CODE_LENGTH = 10
    def create(self, **kwargs):
        """
        handle code creation
        """
        pool = ascii_uppercase + digits + '.-'
        code = kwargs.get('code', ''.join(random.choices(pool, k=self.CODE_LENGTH)))
        while self.filter(code=code).exists():
            code = ''.join(random.choices(pool, k=self.CODE_LENGTH))
        kwargs['code'] = code
        return super(InvitiationManager, self).create(**kwargs)
