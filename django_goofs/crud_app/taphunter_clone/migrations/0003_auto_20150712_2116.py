# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taphunter_clone', '0002_tap_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tap',
            name='bar',
        ),
        migrations.RemoveField(
            model_name='tap',
            name='beer',
        ),
        migrations.AddField(
            model_name='bar',
            name='beers',
            field=models.ManyToManyField(to='taphunter_clone.Beer'),
        ),
        migrations.DeleteModel(
            name='Tap',
        ),
    ]
