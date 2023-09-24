# Generated by Django 4.1.7 on 2023-09-21 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0010_personaldetailsmodel_hello_content'),
    ]

    operations = [
        migrations.CreateModel(
            name='EducationModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(max_length=300)),
                ('clg_name', models.CharField(max_length=300)),
                ('university_board', models.CharField(max_length=100)),
                ('passing_date', models.DateField()),
                ('percentage', models.FloatField()),
            ],
        ),
    ]
