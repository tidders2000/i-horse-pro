# Generated by Django 3.1.3 on 2021-02-06 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('horse', '0019_auto_20210202_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='horse',
            name='Dob',
            field=models.DateField(default='2015-01-01'),
        ),
    ]
