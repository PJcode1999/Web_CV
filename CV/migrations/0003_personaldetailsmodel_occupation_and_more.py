# Generated by Django 4.1.7 on 2023-09-20 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CV', '0002_alter_profilemodel_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='personaldetailsmodel',
            name='occupation',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='personaldetailsmodel',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
