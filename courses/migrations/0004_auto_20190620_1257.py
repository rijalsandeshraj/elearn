# Generated by Django 2.2.2 on 2019-06-20 07:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_auto_20190620_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='overview',
            field=models.TextField(max_length=600),
        ),
    ]
