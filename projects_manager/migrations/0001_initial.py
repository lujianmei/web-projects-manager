# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.CharField(unique=True, max_length=256, verbose_name='唯一标识', serialize=False, primary_key=True)),
                ('title', models.CharField(max_length=256, verbose_name='名称')),
                ('start', models.DateTimeField(verbose_name='开始时间')),
                ('end', models.DateTimeField(verbose_name='结束时间')),
                ('weekstartsmonday', models.BooleanField(default=True, verbose_name='周一开始')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('name', models.CharField(max_length=50, verbose_name='姓名')),
                ('email', models.CharField(max_length=50, verbose_name='邮箱')),
                ('rate', models.IntegerField(verbose_name='工价')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('title', models.CharField(max_length=256, verbose_name='名称')),
                ('complete', models.CharField(max_length=256, verbose_name='完成情况')),
                ('depends', models.CharField(max_length=256, verbose_name='依赖任务')),
                ('duration', models.CharField(max_length=256, verbose_name='周期')),
                ('priority', models.CharField(max_length=256, verbose_name='优先级')),
                ('start', models.DateTimeField(verbose_name='开始时间')),
                ('end', models.DateTimeField(verbose_name='结束时间')),
            ],
        ),
        migrations.CreateModel(
            name='TaskAssign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, verbose_name='ID', serialize=False)),
                ('date_assign', models.DateField()),
                ('resource', models.ForeignKey(to='projects_manager.Resource')),
                ('task', models.ForeignKey(to='projects_manager.Task')),
            ],
        ),
        migrations.AddField(
            model_name='task',
            name='allocate',
            field=models.ManyToManyField(to='projects_manager.Resource', through='projects_manager.TaskAssign'),
        ),
        migrations.AddField(
            model_name='task',
            name='projectid',
            field=models.ForeignKey(to='projects_manager.Project'),
        ),
    ]
