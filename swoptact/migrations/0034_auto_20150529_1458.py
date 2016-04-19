# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('streetcrm', '0033_auto_20150526_1145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='address',
            field=models.ForeignKey(to='streetcrm.Address', null=True, blank=True),
        ),
    ]
