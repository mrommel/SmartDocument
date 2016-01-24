# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0004_timelineentry_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=500)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='added')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=40)),
                ('description', models.CharField(max_length=500)),
                ('image', models.ImageField(null=True, upload_to='media/gallery', blank=True)),
                ('date_added', models.DateTimeField(auto_now_add=True, verbose_name='added')),
                ('date_updated', models.DateTimeField(auto_now=True, verbose_name='updated')),
                ('gallery', models.ForeignKey(blank=True, to='forecast.Gallery', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='timelineentry',
            name='gallery',
            field=models.ForeignKey(blank=True, to='forecast.Gallery', null=True),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='timelineentry',
            name='event_type',
            field=models.CharField(default='T', max_length=1, choices=[('T', 'Text'), ('P', 'Picture'), ('G', 'Gallery')]),
            preserve_default=True,
        ),
    ]
