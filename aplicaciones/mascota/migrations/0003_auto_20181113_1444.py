# Generated by Django 2.1.2 on 2018-11-13 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mascota', '0002_auto_20181112_1854'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(upload_to=''),
        ),
    ]
