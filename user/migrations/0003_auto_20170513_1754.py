# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-13 17:54
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_example'),
    ]

    operations = [
        migrations.CreateModel(
            name='Aboutus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email地址')),
                ('tel', models.CharField(max_length=20, verbose_name='电话号码')),
                ('fax', models.CharField(max_length=20, verbose_name='传真')),
                ('phone', models.CharField(max_length=20, verbose_name='移动电话')),
                ('address', models.CharField(max_length=100, verbose_name='地址')),
                ('context', DjangoUeditor.models.UEditorField(default='', verbose_name='公司介绍')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('category', models.ForeignKey(default='aboutus', on_delete=django.db.models.deletion.CASCADE, to='user.Category', verbose_name='文章分类')),
            ],
            options={
                'verbose_name': '关于我们',
                'verbose_name_plural': '关于我们',
            },
        ),
        migrations.AlterField(
            model_name='example',
            name='category',
            field=models.ForeignKey(default='examples', on_delete=django.db.models.deletion.CASCADE, to='user.Category', verbose_name='文章分类'),
        ),
    ]