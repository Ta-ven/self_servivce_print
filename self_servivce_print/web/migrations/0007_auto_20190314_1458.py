# Generated by Django 2.1.7 on 2019-03-14 14:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20190314_1450'),
    ]

    operations = [
        migrations.AlterField(
            model_name='time',
            name='add_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='time',
            name='mod_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
