# Generated by Django 4.1.10 on 2023-08-15 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0002_alter_companymodel_website'),
    ]

    operations = [
        migrations.AlterField(
            model_name='companydocumentsmodel',
            name='companyId',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='company_document', to='companies.companymodel'),
        ),
    ]