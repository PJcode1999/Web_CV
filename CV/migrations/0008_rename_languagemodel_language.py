# Generated by Django 4.1.7 on 2023-09-20 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0007_remove_personaldetailsmodel_language_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='LanguageModel',
            new_name='Language',
        ),
    ]
