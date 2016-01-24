# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0013_auto_20160123_2105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uuid',
            field=models.CharField(default='07918e2a-7a2d-46ec-8edc-c54109296d47', max_length=36, editable=False, blank=True),
            preserve_default=True,
        ),
    ]
