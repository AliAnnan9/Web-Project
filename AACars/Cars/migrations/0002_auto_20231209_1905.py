# Generated by Django 3.1 on 2023-12-09 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='image1',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image2',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image3',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image4',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image5',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='car',
            name='image6',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
