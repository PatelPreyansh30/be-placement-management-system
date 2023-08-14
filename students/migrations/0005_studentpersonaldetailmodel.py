# Generated by Django 4.1.10 on 2023-08-14 16:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('students', '0004_alter_studentcollegedetailmodel_currentbacklog_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentPersonalDetailModel',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('whatsappMobile', models.CharField(max_length=150)),
                ('alternateMobile', models.CharField(max_length=150)),
                ('address', models.TextField()),
                ('profilePic', models.FileField(upload_to='student_profile_pic/')),
                ('resume', models.FileField(upload_to='student_resumes/')),
                ('createdAt', models.DateTimeField(auto_now_add=True)),
                ('updatedAt', models.DateTimeField(auto_now=True)),
                ('studentId', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
