# Generated by Django 3.1 on 2023-12-09 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=255)),
                ('Manufactur', models.CharField(max_length=255)),
                ('Model', models.CharField(max_length=255)),
                ('Year', models.CharField(max_length=255)),
                ('Milage', models.CharField(max_length=255)),
                ('Color', models.CharField(max_length=255)),
                ('Engine', models.CharField(max_length=255)),
                ('Power', models.CharField(max_length=255)),
                ('Torque', models.CharField(max_length=255)),
                ('Transmission', models.CharField(max_length=255)),
                ('DriveType', models.CharField(max_length=255)),
                ('image1', models.CharField(max_length=255)),
                ('image2', models.CharField(max_length=255)),
                ('image3', models.CharField(max_length=255)),
                ('image4', models.CharField(max_length=255)),
                ('image5', models.CharField(max_length=255)),
                ('image6', models.CharField(max_length=255)),
            ],
        ),
    ]
