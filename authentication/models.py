from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ConpecUser(models.Model):
    user = models.OneToOneField(User)
    ra = models.CharField(max_length=6)

    def __str__(self):
        return "%s-%s" % (self.user, self.ra)
