# Generated by Django 4.1.7 on 2023-09-21 17:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0013_educationmodel_clg_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='educationmodel',
            name='profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CV.personaldetailsmodel'),
        ),
    ]
