# Generated by Django 4.0.6 on 2022-08-02 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('IOT', '0005_recyclers_average_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='weight_height',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
