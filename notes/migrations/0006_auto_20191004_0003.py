# Generated by Django 2.2.5 on 2019-10-03 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0005_post_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]