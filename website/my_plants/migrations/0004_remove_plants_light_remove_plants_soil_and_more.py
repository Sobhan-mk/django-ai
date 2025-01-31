# Generated by Django 5.1.4 on 2025-01-14 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_plants', '0003_plants_plant_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='plants',
            name='light',
        ),
        migrations.RemoveField(
            model_name='plants',
            name='soil',
        ),
        migrations.RemoveField(
            model_name='plants',
            name='temperature',
        ),
        migrations.RemoveField(
            model_name='plants',
            name='water',
        ),
        migrations.AddField(
            model_name='plants',
            name='conditions',
            field=models.TextField(default=''),
        ),
        migrations.AddField(
            model_name='plants',
            name='family',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='plants',
            name='genus',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='plants',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='plants',
            name='persian_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='plants',
            name='scientific_name',
            field=models.CharField(default='', max_length=200, unique=True),
        ),
    ]
