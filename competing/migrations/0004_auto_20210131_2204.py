# Generated by Django 3.1.3 on 2021-01-31 22:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competing', '0003_auto_20210131_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='competitionlog',
            name='date',
            field=models.DateTimeField(null=True),
        ),
    ]