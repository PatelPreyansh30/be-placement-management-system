# Generated by Django 4.1.10 on 2023-08-15 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0005_studentpersonaldetailmodel'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentpersonaldetailmodel',
            name='profilePic',
            field=models.ImageField(upload_to='student_profile_pic/'),
        ),
    ]
