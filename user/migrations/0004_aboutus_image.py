# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-13 19:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20170513_1754'),
    ]

    operations = [
        migrations.AddField(
            model_name='aboutus',
            name='image',
            field=models.ImageField(default='1', upload_to='img/%Y/%m', verbose_name='地点截图'),
        ),
    ]