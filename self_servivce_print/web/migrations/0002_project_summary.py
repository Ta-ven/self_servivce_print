# Generated by Django 2.1.7 on 2019-03-14 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='summary',
            field=models.CharField(default='dadada', max_length=64),
            preserve_default=False,
        ),
    ]