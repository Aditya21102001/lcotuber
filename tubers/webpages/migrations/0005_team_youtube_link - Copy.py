# Generated by Django 3.1.4 on 2020-12-19 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0004_auto_20201219_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='youtube_link',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]