# Generated by Django 4.1.7 on 2023-09-20 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0003_personaldetailsmodel_occupation_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetailsmodel',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldetailsmodel',
            name='phone',
            field=models.CharField(default=1, max_length=15),
            preserve_default=False,
        ),
    ]
