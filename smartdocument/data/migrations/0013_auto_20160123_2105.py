# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0012_auto_20160117_1653'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uuid',
            field=models.CharField(default='417fc239-f0a7-43e5-bd2c-8403b845f7b7', max_length=36, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
