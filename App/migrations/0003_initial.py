# Generated by Django 4.0.3 on 2022-03-24 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('App', '0002_delete_test'),
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder', models.FileField(upload_to='')),
            ],
        ),
    ]
