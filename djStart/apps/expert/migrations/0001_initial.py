# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-24 09:23
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('message', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Expert',
            fields=[
                ('username', models.OneToOneField(db_column='username', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL, verbose_name='用户帐号')),
                ('expert_number', models.CharField(blank=True, max_length=8, null=True, verbose_name='专家证书编号')),
                ('valid_time', models.CharField(blank=True, max_length=11, null=True, verbose_name='证书有效时间')),
                ('name', models.CharField(blank=True, max_length=20, null=True, verbose_name='证书有效时间')),
                ('gender', models.CharField(blank=True, choices=[('male', '男'), ('female', '女')], default='male', max_length=10, null=True, verbose_name='性别')),
                ('birthday', models.CharField(blank=True, max_length=11, null=True, verbose_name='出生日期')),
                ('politic', models.CharField(blank=True, max_length=20, null=True, verbose_name='政治面貌')),
                ('certificate_type', models.CharField(blank=True, choices=[('i.d.card', '身份证'), ('student card', '学生证'), ('passport', '学生证')], default='i.d.card', max_length=20, null=True, verbose_name='证件类型')),
                ('certificate_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='证件号')),
                ('phone_number', models.CharField(blank=True, max_length=20, null=True, verbose_name='电话号码')),
                ('email', models.EmailField(blank=True, max_length=20, null=True, verbose_name='邮箱')),
                ('picture', models.ImageField(blank=True, default='image/default/', null=True, upload_to='image/%Y/%m', verbose_name='照片')),
                ('state', models.CharField(blank=True, choices=[('undo', '待填表'), ('done', '待审核'), ('denied', '驳回申请'), ('checked', '已审核')], default='undo', max_length=10, null=True)),
            ],
            options={
                'verbose_name_plural': '专家信息表',
                'verbose_name': '专家信息表',
                'db_table': 'Expert',
            },
        ),
    ]
