# Generated by Django 4.0.6 on 2022-07-25 12:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('IOT', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dustbin',
            old_name='latitude',
            new_name='latitude_longitude',
        ),
        migrations.RemoveField(
            model_name='dustbin',
            name='longitude',
        ),
    ]
