# Generated by Django 4.0.3 on 2022-03-25 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0010_remove_drive_extension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drive',
            name='size',
            field=models.IntegerField(default=''),
        ),
    ]
