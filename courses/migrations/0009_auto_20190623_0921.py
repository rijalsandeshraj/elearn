# Generated by Django 2.2.2 on 2019-06-23 03:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0008_auto_20190620_1415'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='file',
        ),
        migrations.RemoveField(
            model_name='course',
            name='preview',
        ),
    ]
