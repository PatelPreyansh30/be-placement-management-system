# Generated by Django 4.1.10 on 2023-08-15 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faculty', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facultypersonalmodel',
            name='profilePic',
            field=models.ImageField(upload_to='faculty_profile_pic/'),
        ),
    ]
