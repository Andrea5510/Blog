# Generated by Django 4.0.3 on 2022-04-24 23:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_login', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='avatar',
            name='imagen',
        ),
    ]
