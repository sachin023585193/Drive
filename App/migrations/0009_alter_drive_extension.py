# Generated by Django 4.0.3 on 2022-03-25 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_rename_file_drive_file_drive_extension_drive_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drive',
            name='extension',
            field=models.CharField(default=0, max_length=40),
        ),
    ]
