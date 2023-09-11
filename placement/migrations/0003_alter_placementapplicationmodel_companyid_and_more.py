# Generated by Django 4.1.10 on 2023-09-11 17:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0004_alter_companydocumentsmodel_companyid'),
        ('placement', '0002_alter_placementapplicationmodel_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='placementapplicationmodel',
            name='companyId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appliedCompany', to='companies.companymodel'),
        ),
        migrations.AlterField(
            model_name='placementapplicationmodel',
            name='status',
            field=models.CharField(choices=[('applied', 'Applied'), ('interviewed', 'Interviewed'), ('placed', 'Placed')], default='applied', max_length=20),
        ),
    ]
