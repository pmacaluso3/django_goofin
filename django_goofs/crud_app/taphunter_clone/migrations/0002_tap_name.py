# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('taphunter_clone', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tap',
            name='name',
            field=models.CharField(default='some tap', max_length=200),
            preserve_default=False,
        ),
    ]
