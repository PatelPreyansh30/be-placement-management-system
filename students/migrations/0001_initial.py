# Generated by Django 4.1.10 on 2023-08-12 17:54

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StudentProfileModel',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=50)),
                ('lastName', models.CharField(max_length=50)),
                ('mobile', models.CharField(max_length=50)),
                ('whatsappMobile', models.CharField(max_length=50)),
                ('alternateMobile', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('city', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StudentEducationModel',
            fields=[
                ('id', models.UUIDField(auto_created=True, default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('schoolingMedium', models.CharField(choices=[('GUJ', 'Gujarati'), ('ENG', 'English'), ('HN', 'Hindi')], max_length=50)),
                ('studentId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='students.studentprofilemodel')),
            ],
        ),
    ]