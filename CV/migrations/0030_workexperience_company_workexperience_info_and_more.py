# Generated by Django 4.1.7 on 2023-09-22 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0029_alter_workduration_enddate_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='workexperience',
            name='company',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workexperience',
            name='info',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workexperience',
            name='technology',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
