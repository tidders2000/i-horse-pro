# Generated by Django 3.1.3 on 2021-04-06 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('competing', '0009_auto_20210308_1751'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comphorse',
            name='class_time',
            field=models.TimeField(blank=True),
        ),
    ]
