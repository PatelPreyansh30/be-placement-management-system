# Generated by Django 4.1.10 on 2023-08-28 16:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('faculty', '0002_alter_facultypersonalmodel_profilepic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultypersonalmodel',
            name='facultyId',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='facultyDetail', to=settings.AUTH_USER_MODEL),
        ),
    ]
