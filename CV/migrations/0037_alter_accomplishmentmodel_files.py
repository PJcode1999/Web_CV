# Generated by Django 5.1.5 on 2025-02-06 05:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0036_rename_sorce_accomplishmentmodel_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomplishmentmodel',
            name='files',
            field=models.ImageField(upload_to='Web_CV/staticfiles/admin/img'),
        ),
    ]
