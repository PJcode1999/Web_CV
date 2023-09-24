# Generated by Django 4.1.7 on 2023-09-20 17:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0005_alter_personaldetailsmodel_marital_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='languagemodel',
            name='profile',
        ),
        migrations.AddField(
            model_name='personaldetailsmodel',
            name='language',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='CV.languagemodel'),
            preserve_default=False,
        ),
    ]
