# Generated by Django 4.1.10 on 2023-08-12 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_studentcollegedetailmodel_studentpersonaldetailmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentcollegedetailmodel',
            name='enrollmentNumber',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]
