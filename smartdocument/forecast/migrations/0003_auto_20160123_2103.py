# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0002_payment'),
    ]

    operations = [
        migrations.CreateModel(
            name='TimelineEntry',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=500)),
                ('event_type', models.CharField(default='T', max_length=1, choices=[('T', 'Text'), ('P', 'Picture')])),
                ('image', models.ImageField(null=True, upload_to='media/timeline', blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='added')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='payment',
            name='period',
            field=models.CharField(default='O', max_length=1, choices=[('O', 'Once'), ('M', 'Monthly'), ('Q', 'Quarterly'), ('Y', 'Yearly')]),
            preserve_default=True,
        ),
    ]
