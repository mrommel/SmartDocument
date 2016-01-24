# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0014_auto_20160123_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uuid',
            field=models.CharField(default='26b594cc-c034-49ac-9a45-a4ff76fa7808', max_length=36, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
