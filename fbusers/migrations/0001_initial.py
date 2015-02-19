# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FbUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=128)),
                ('facebookId', models.CharField(unique=True, max_length=32)),
                ('name', models.CharField(max_length=256)),
                ('gender', models.CharField(max_length=8)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FbUserLog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('action', models.CharField(max_length=8, choices=[('created', 'New register'), ('updated', 'Register Updated'), ('deleted', 'Register deleted'), ('error', 'API error')])),
                ('facebookId', models.CharField(max_length=32)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('error_code', models.CharField(max_length=32, null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
