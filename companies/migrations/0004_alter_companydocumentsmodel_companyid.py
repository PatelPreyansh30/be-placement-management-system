# Generated by Django 4.1.10 on 2023-09-05 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0003_alter_companydocumentsmodel_companyid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydocumentsmodel',
            name='companyId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='companyDocument', to='companies.companymodel'),
        ),
    ]
