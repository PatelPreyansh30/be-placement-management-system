# Generated by Django 4.1.10 on 2023-10-01 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_studentmodel_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='schoolMedium',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='studentmodel',
            name='twelvePercent',
            field=models.DecimalField(decimal_places=2, max_digits=4),
        ),
    ]
