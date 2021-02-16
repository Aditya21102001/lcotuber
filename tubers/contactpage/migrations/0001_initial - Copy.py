# Generated by Django 3.1.4 on 2020-12-24 17:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contactpage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(blank=True, max_length=100)),
                ('subject', models.TextField()),
                ('city', models.CharField(blank=True, max_length=100)),
                ('phone', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=255)),
                ('state', models.CharField(blank=True, max_length=100)),
                ('message', models.TextField(blank=True)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
