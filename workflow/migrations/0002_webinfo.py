# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2018-01-30 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workflow', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WebInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('site_name', models.CharField(max_length=128, verbose_name='\u7ad9\u70b9\u540d')),
                ('site_value', models.CharField(max_length=128, verbose_name='\u7ad9\u70b9\u503c')),
            ],
        ),
    ]