# Generated by Django 4.1.7 on 2023-09-21 03:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0009_philosophymodel_points'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetailsmodel',
            name='hello_content',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]
