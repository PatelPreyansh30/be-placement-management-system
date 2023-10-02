# Generated by Django 4.1.10 on 2023-10-01 17:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0002_branchmodel'),
    ]

    operations = [
        migrations.RenameField(
            model_name='branchmodel',
            old_name='label',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='collegemodel',
            old_name='label',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='branchmodel',
            name='value',
        ),
        migrations.RemoveField(
            model_name='collegemodel',
            name='value',
        ),
    ]
