# Generated by Django 2.2.5 on 2019-09-24 16:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0003_auto_20190923_1254'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date_modified',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
