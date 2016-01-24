# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0015_auto_20160123_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uuid',
            field=models.CharField(default='bbfff28f-07e8-4b07-aa8f-2ed273a22e4f', max_length=36, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
