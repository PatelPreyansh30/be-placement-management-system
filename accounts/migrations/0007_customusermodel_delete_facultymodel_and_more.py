# Generated by Django 4.1.10 on 2023-08-14 14:09

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_facultymodel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUserModel',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=150)),
                ('lastName', models.CharField(max_length=150)),
                ('mobile', models.CharField(max_length=150, unique=True)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('password', models.CharField(max_length=150)),
                ('isStudent', models.BooleanField(default=False)),
                ('isFaculty', models.BooleanField(default=False)),
                ('isAdmin', models.BooleanField(default=False)),
                ('isVerified', models.BooleanField(default=False)),
                ('isBlocked', models.BooleanField(default=False)),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='FacultyModel',
        ),
        migrations.DeleteModel(
            name='StudentModel',
        ),
    ]
