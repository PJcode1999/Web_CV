# Generated by Django 5.1.5 on 2025-02-06 06:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0038_alter_accomplishmentmodel_files'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accomplishmentmodel',
            name='files',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
