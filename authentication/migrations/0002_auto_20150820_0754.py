# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='conpecuser',
            name='ra',
            field=models.CharField(default=None, max_length=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='conpecuser',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default=None),
            preserve_default=False,
        ),
    ]
