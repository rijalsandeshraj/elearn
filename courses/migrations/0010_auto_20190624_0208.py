# Generated by Django 2.2.2 on 2019-06-23 20:23

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('courses', '0009_auto_20190623_0921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='group',
        ),
        migrations.AddField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses_joined', to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='Group',
        ),
    ]
