# Generated by Django 3.1 on 2023-12-18 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FilmCar', '0003_appointment_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='car',
        ),
        migrations.AddField(
            model_name='appointment',
            name='Time',
            field=models.TimeField(null=True),
        ),
    ]
