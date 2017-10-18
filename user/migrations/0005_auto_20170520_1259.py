# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-20 12:59
from __future__ import unicode_literals

import DjangoUeditor.models
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_aboutus_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Important',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('image', models.ImageField(upload_to='img/%Y/%m', verbose_name='首页大图')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': '首页大图',
                'verbose_name': '首页大图',
            },
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='文章标题')),
                ('tag', models.CharField(max_length=10, verbose_name='标签')),
                ('describe', models.CharField(max_length=255, verbose_name='描述')),
                ('image', models.ImageField(upload_to='img/%Y/%m', verbose_name='文章图示')),
                ('context', DjangoUeditor.models.UEditorField(default='', verbose_name='文章内容')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('click_count', models.IntegerField(default=0, verbose_name='点击数')),
            ],
            options={
                'verbose_name_plural': '新闻动态',
                'verbose_name': '新闻动态',
            },
        ),
        migrations.CreateModel(
            name='NewsCate',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='分类ID')),
                ('name', models.CharField(max_length=50, verbose_name='分类')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name_plural': '分类信息',
                'verbose_name': '分类信息',
            },
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('describe', models.CharField(max_length=255, verbose_name='描述')),
                ('image', models.ImageField(upload_to='img/%Y/%m', verbose_name='案例图片')),
                ('context', DjangoUeditor.models.UEditorField(default='', verbose_name='文章内容')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name_plural': '产品展示',
                'verbose_name': '产品展示',
            },
        ),
        migrations.CreateModel(
            name='SolutionCate',
            fields=[
                ('id', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='分类ID')),
                ('name', models.CharField(max_length=50, verbose_name='文章分类')),
                ('created_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('last_modified_time', models.DateTimeField(auto_now=True, verbose_name='修改时间')),
            ],
            options={
                'verbose_name_plural': '分类信息',
                'verbose_name': '分类信息',
            },
        ),
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='标题')),
                ('describe', models.CharField(max_length=255, verbose_name='描述')),
                ('image', models.ImageField(upload_to='img/%Y/%m', verbose_name='文章图示')),
                ('context', DjangoUeditor.models.UEditorField(default='', verbose_name='文章内容')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('update_time', models.DateTimeField(auto_now=True, null=True)),
                ('solutionCate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.SolutionCate', verbose_name='解决方案分类')),
            ],
            options={
                'verbose_name_plural': '解决方案',
                'verbose_name': '解决方案',
            },
        ),
        migrations.RenameModel(
            old_name='Category',
            new_name='ProductCate',
        ),
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.AlterModelOptions(
            name='example',
            options={'verbose_name': '客户案例', 'verbose_name_plural': '客户案例'},
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='address',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='category',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='email',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='fax',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='aboutus',
            name='tel',
        ),
        migrations.RemoveField(
            model_name='example',
            name='category',
        ),
        migrations.RemoveField(
            model_name='example',
            name='click_count',
        ),
        migrations.RemoveField(
            model_name='example',
            name='tag',
        ),
        migrations.AddField(
            model_name='aboutus',
            name='title',
            field=models.CharField(default=django.utils.timezone.now, max_length=255, verbose_name='标题'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.AddField(
            model_name='products',
            name='productCate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.ProductCate', verbose_name='分类'),
        ),
        migrations.AddField(
            model_name='news',
            name='newsCate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.NewsCate', verbose_name='文章分类'),
        ),
    ]
