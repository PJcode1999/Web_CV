# Generated by Django 4.1.7 on 2023-09-21 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0014_alter_educationmodel_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationmodel',
            name='percentage',
            field=models.CharField(max_length=50),
        ),
    ]
