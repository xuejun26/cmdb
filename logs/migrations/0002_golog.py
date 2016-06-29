# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-29 15:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('logs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='goLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=100)),
                ('remote_ip', models.GenericIPAddressField()),
                ('goAction', models.TextField()),
                ('result', models.TextField(default='')),
                ('datetime', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]