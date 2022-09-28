# Generated by Django 4.1 on 2022-09-07 14:50

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('first_name', models.CharField(default=None, max_length=20, null=True)),
                ('last_name', models.CharField(default=None, max_length=20, null=True)),
                ('middle_name', models.CharField(default=None, max_length=20, null=True)),
                ('email', models.EmailField(default=None, max_length=100, null=True, unique=True)),
                ('username', models.CharField(blank=True, default=models.EmailField(default=None, max_length=100, null=True, unique=True), max_length=100, null=True)),
                ('password', models.CharField(default=None, max_length=255, null=True)),
                ('created_at', models.DateTimeField(auto_now=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('role', models.IntegerField(choices=[(0, 'visitor'), (1, 'admin')], default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]